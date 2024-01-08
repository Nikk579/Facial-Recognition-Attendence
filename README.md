# Facial Recognition Attendance System

This project is a simple facial recognition attendance system implemented in Python using the face_recognition library.
The system captures video from the default camera, recognizes faces, and tracks attendance based on known faces.

## Features

- Real-time facial recognition
- Attendance tracking with date and time
- Support for multiple known faces

## Requirements

Make sure you have the following dependencies installed:

- Python 3.x
- OpenCV
- face_recognition
- NumPy

You can install the required packages using the following command:

```bash
pip install -r requirements.txt
```

 ## Usage
Clone the repository:

```
git clone https://github.com/your-username/your-repo.git
```

## Run the program:

```
python main.py
```

Press 'q' to exit the application.

## Configuration
Modify the images in the 'faces' directory with the faces you want to recognize.

Update the known_face_names list in main.py with corresponding names.

Customize the bottomLeftCornerOfText variable in main.py to change the position of displayed text.

