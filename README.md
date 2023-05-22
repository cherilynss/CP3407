# CP3407 Advanced Software Engineering

Made by Raj Choudhury, Cherilyn Susanto and Huynh Truong Thien Duong.

### Face Recognition Attendance System
This project implements a Face Recognition Attendance System using computer vision techniques and machine learning algorithms. The system allows for real-time face recognition and attendance tracking based on the detected faces.

### Features
1. Real-time face recognition: The system uses the OpenCV library to capture video frames from a camera and performs face detection using the Haar cascade classifier.
2. Face identification: Once a face is detected, the system utilizes a pre-trained machine learning model to identify the person based on the captured face. The model is trained using the K-Nearest Neighbors algorithm.
3. Attendance tracking: The system maintains a CSV file that records the attendance of individuals. Each attendance entry includes the person's name, roll number, and the time of attendance.
4. Web interface: The system provides a web interface built with Flask, where users can view the attendance records, register new faces, and start the face recognition process.


### Prerequisites
Before running the application, ensure that you have the following dependencies installed:

* Python (version 3.7 or above)
* OpenCV (cv2)
* Flask
* NumPy
* scikit-learn
* pandas

### Usage

Register Faces:

* Click on the "Add New User" button on the web interface.
* Enter the username and roll number of the person to be registered.
* Follow the instructions to capture 50 images of the person's face. Make sure the person's face is well-illuminated and visible in the camera frame.
* Once the images are captured, the system will train a face recognition model using the captured images.

Start Face Recognition:

* Click on the "Start Recognition" button on the web interface.
* The system will start the real-time face recognition process using the trained model.
* Detected faces will be displayed on the screen with the identified person's name.
* The system will automatically record the attendance of the identified person in the CSV file.



To stop the application, press Ctrl+C in the terminal or command prompt.