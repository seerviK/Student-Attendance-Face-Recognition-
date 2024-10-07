import os
import pickle
import numpy as np
import cv2
import face_recognition
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from datetime import datetime

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-fda4d-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendancerealtime-fda4d.appspot.com"
})

bucket = storage.bucket()

# Video capture settings
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height

# Load the encoding file
print("Loading Encode File ...")
with open('EncodeFile.p', 'rb') as file:
    encodeListKnownWithIds = pickle.load(file)
encodeListKnown, studentIds = encodeListKnownWithIds
print("Encode File Loaded")

modeType = 0
counter = 0
id = -1
imgStudent = []
frame_skip = 5  # Process every 5th frame
frame_count = 0

while True:
    success, img = cap.read()

    # To reduce lag, skip frames to decrease the load
    frame_count += 1
    if frame_count % frame_skip != 0:
        # Skip this frame
        continue

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)  # Resize frame for faster processing
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)  # Convert to RGB for face_recognition

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    if faceCurFrame:
        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4  # Scale back up face coordinates
                bbox = x1, y1, x2 - x1, y2 - y1
                img = cvzone.cornerRect(img, bbox, rt=0)  # Draw rectangle around the face
                id = studentIds[matchIndex]

                if counter == 0:
                    cvzone.putTextRect(img, "Loading", (275, 400))
                    cv2.imshow("Face Attendance", img)
                    cv2.waitKey(1)
                    counter = 1
                    modeType = 1

        if counter != 0:
            if counter == 1:
                # Get the student's data from the Firebase Realtime Database
                studentInfo = db.reference(f'Students/{id}').get()
                print(studentInfo)

                # Get the student's image from Firebase Storage
                blob = bucket.get_blob(f'Images/{id}.png')
                array = np.frombuffer(blob.download_as_string(), np.uint8)
                imgStudent = cv2.imdecode(array, cv2.IMREAD_COLOR)

                # Update attendance in the database if 30 seconds have passed since last attendance
                last_attendance_time = datetime.strptime(studentInfo['last_attendance_time'], "%Y-%m-%d %H:%M:%S")
                secondsElapsed = (datetime.now() - last_attendance_time).total_seconds()
                if secondsElapsed > 30:
                    ref = db.reference(f'Students/{id}')
                    studentInfo['total_attendance'] += 1
                    ref.child('total_attendance').set(studentInfo['total_attendance'])
                    ref.child('last_attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

            # Display student information for up to 10 frames
            if counter <= 10:
                cv2.putText(img, f"Attendance: {studentInfo['total_attendance']}", (20, 50),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
                cv2.putText(img, f"Major: {studentInfo['major']}", (20, 100),
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                cv2.putText(img, f"ID: {id}", (20, 150),
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                cv2.putText(img, f"Standing: {studentInfo['standing']}", (20, 200),
                            cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                cv2.putText(img, f"Year: {studentInfo['year']}", (20, 250),
                            cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                cv2.putText(img, f"Start Year: {studentInfo['starting_year']}", (20, 300),
                            cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)

                (w, h), _ = cv2.getTextSize(studentInfo['name'], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                cv2.putText(img, f"Name: {studentInfo['name']}", (20, 350),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 1)

                if imgStudent is not None:
                    img[50:50 + imgStudent.shape[0], 300:300 + imgStudent.shape[1]] = imgStudent

            counter += 1

            if counter >= 20:
                counter = 0
                modeType = 0
                studentInfo = []
                imgStudent = []
    else:
        modeType = 0
        counter = 0

    cv2.imshow("Face Attendance", img)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
