import cv2  # Import OpenCV library
import csv  # Import CSV module for working with CSV files
import numpy as np  # Import NumPy library for numerical operations
import face_recognition  # Import face_recognition library for face recognition functionality
from datetime import datetime  # Import datetime module for working with dates and times

# Initialize video capture from the default camera (camera index 0)
video_capture = cv2.VideoCapture(0)

# Load and encode facial images
nikhil_image = face_recognition.load_image_file("faces/nikhil.jpeg")
nikhil_encoded = face_recognition.face_encodings(nikhil_image)[0]
gaurav_image = face_recognition.load_image_file("faces/gaurav.jpg")
gaurav_encoded = face_recognition.face_encodings(gaurav_image)[0]

# Create lists of known face encodings and names
known_face_encodings = [nikhil_encoded, gaurav_encoded]
known_face_names = ["Nikhil", "Gaurav"]

# Create a copy of known face names for tracking students' attendance
students = known_face_names.copy()

# Initialize variables for face locations, encodings, and current date
face_locations = []
face_encodings = []
now = datetime.now()
current_date = now.strftime("%d-%m-%Y")

# Open a CSV file for writing attendance data
f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

# Infinite loop for real-time face recognition
while True:
    _, frame = video_capture.read()

    # Resize the frame if it is not empty
    if not frame is None:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    else:
        continue

    # Convert color to RGB for face recognition
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognize faces in the frame
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    # Loop through recognized faces
    for face_encoding in face_encodings:
        # Compare face encodings with known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distances = [np.linalg.norm(np.array(face_encoding) - np.array(known_face_encoding)) for known_face_encoding in known_face_encodings]
        best_match_index = np.argmin(face_distances)

        # If there's a match, get the corresponding name
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # If the name is in the known face names list
        if name in known_face_names:
            # Set up text properties for displaying on the frame
            font = cv2.FONT_HERSHEY_TRIPLEX
            bottomLeftCornerOfText = (10, 30)
            fontScale = 1.5
            fontColor = (255, 0, 0)
            thickness = 3
            lineType = 2

            # Display name and "present" on the frame
            cv2.putText(frame, f"{name} present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

            # If the student is in the list, remove them and record attendance
            if name in students:
                students.remove(name)
                current_time = now.strftime("%I-%M-%S %p")
                lnwriter.writerow([name, current_time])

    # Display the frame with face recognition information
    cv2.imshow("Attendance", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture object and close all windows
video_capture.release()
cv2.destroyAllWindows()

# Close the CSV file
f.close()
