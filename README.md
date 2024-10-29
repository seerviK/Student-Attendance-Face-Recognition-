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


Memory updated
Here’s a professional and visually engaging README file for your Flappy Bird game project:

Flappy Bird Game 🎮
Welcome to Flappy Bird—a fun and interactive browser game that brings the popular bird-flying mechanics to life using HTML, CSS, and JavaScript. The game challenges players to navigate a bird through a series of pipes without hitting them, keeping track of scores and incorporating physics-based movement.



🎯 Features
Realistic Gravity and Jump Mechanics: The bird falls due to gravity, and pressing Space or Arrow Up allows the bird to jump.
Dynamic Pipes: Pipes appear at intervals with random gaps, making the game progressively challenging.
Score Counter: Keeps track of the score as you pass through pipe pairs.
Game Over Screen: Clearly displayed when the bird collides with a pipe or goes off-screen.
📁 Project Structure
HTML: Provides the structure of the game display.
CSS: Styles the game, giving it a clean, polished look.
JavaScript: Manages game logic, including bird physics, pipe placement, collision detection, and score tracking.
🕹️ How to Play
Start the Game: Open the HTML file in a web browser.
Control the Bird: Press Space, Arrow Up, or X to make the bird jump.
Avoid Pipes: Navigate through the pipes to keep scoring. Hitting a pipe or falling ends the game.
Restart: Press any jump key after a game over to restart.
💻 Installation
Clone this repository to your local machine:
bash
Copy code
git clone https://github.com/your-username/flappy-bird-game.git
Navigate to the project folder:
bash
Copy code
cd flappy-bird-game
Open index.html in your preferred web browser to start playing!
🛠️ Technologies Used
HTML5 Canvas: For rendering graphics.
JavaScript: For game functionality, physics, and interactions.
CSS: For styling the game canvas and UI.
📸 Screenshots

📈 Future Improvements
Responsive Design: Adapting the game for mobile devices.
Sound Effects: Adding sound for jumps and game-over events.
Leaderboard: Track and display high scores.
👤 Author
Kamlesh Choudhary
GitHub: https://github.com/seerviK
LinkedIn: www.linkedin.com/in/kamlesh-choudhary-775512257
