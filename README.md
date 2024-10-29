Face Recognition Attendance Management System
A real-time attendance management system that leverages face recognition technology and Firebase integration to automatically log attendance by recognizing students' faces. This project ensures a seamless and efficient way to track attendance without manual inputs, providing a valuable tool for institutions looking to modernize attendance management.

📜 Project Overview
This project utilizes a combination of Python, OpenCV, and Firebase to build a robust face recognition system. It captures images from a video feed, identifies known faces, and records attendance data in a Firebase database. The system updates attendance in real-time and ensures reliable tracking for each student.

⚙️ Key Features
 - Real-Time Face Recognition: Detects and matches faces in real-time using a camera feed.
 - Firebase Integration: Stores and retrieves student information and attendance records in Firebase Realtime Database and Firebase Storage.
 - Automatic Attendance Logging: Updates the attendance record if a student is recognized and has been absent for more than 30 seconds.
 - Data Encryption and Serialization: Face encodings are saved in a serialized format for fast processing and secure storage.
 - User-Friendly GUI: Displays student information alongside their attendance status in real-time.

![image](https://github.com/user-attachments/assets/d63071d1-553a-403d-a758-787619d08be0)

🛠️ Technologies Used
 - Python: Main programming language.
 - OpenCV: Image and video processing library.
 - face_recognition: Python library for facial recognition.
 - Firebase: Backend database for storing student information and attendance records.

📂 Project Structure
 - main.py: The core script that handles face recognition, attendance logging, and data display.
 - AddDataToDatabase.py: Script to add initial student data to the Firebase Realtime Database.
 - EncodeGenerator.py: Generates and stores face encodings, which are later used for face recognition.

📋 Prerequisites
 1. Install the necessary Python libraries:
 bash
  pip install opencv-python-headless numpy face-recognition firebase-admin cvzone
 2. Set up Firebase:
 - Create a Firebase project and obtain the serviceAccountKey.json.
 - Configure Firebase Realtime Database and Firebase Storage.

🚀 Getting Started
1. Clone the Repository:
   git clone https://github.com/seerviK/Student-Attendance-Face-Recognition.git
2. Prepare Student Images:
   Add each student’s image in the Images folder with the image named as their unique ID.
3. Run Encode Generation:
   Generate face encodings and upload student images to Firebase Storage by running:
   python EncodeGenerator.py
4. Add Student Data to Database:
   Add initial student information (name, ID, year, attendance status) to Firebase by running:
   python AddDataToDatabase.py
5. Start the Attendance System:
   Capture and recognize faces in real-time to record attendance by running:
   python main.py

📑 Code Explanation
 - main.py:
   Initializes Firebase, sets up video capture, and continuously scans faces.
   Matches recognized faces with stored encodings to identify students and update attendance.
   Displays real-time information, including attendance count and last attendance time.
 - AddDataToDatabase.py:
   Loads student data into Firebase, initializing records with attendance and other metadata.
 - EncodeGenerator.py:
   Loads student images, encodes them, and saves the encodings in a serialized file for fast retrieval.

✨ Future Improvements
 - Add support for multiple cameras.
 - Enhance face recognition accuracy.
 - Develop a web interface for remote monitoring and attendance reports.

👤 Author
Kamlesh Choudhary
GitHub: https://github.com/seerviK
LinkedIn: www.linkedin.com/in/kamlesh-choudhary-775512257
