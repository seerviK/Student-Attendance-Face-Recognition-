import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-fda4d-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
"444555":
        {
            "name": "Kamlesh Choudhary",
            "major": "CS",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2024-09-11 00:54:34"
        },
    "102030":
        {
            "name": "MS Dhoni",
            "major": "WK",
            "starting_year": 2022,
            "total_attendance": 12,
            "standing": "B",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "203040":
        {
            "name": "Rohit Sharma",
            "major": "Opener",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "333444":
        {
            "name": "Akshay Rupanvar",
            "major": "Mechanical",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "554466":
        {
            "name": "Virat Kohli",
            "major": "Batsmen",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "100200":
        {
            "name": "Rohit Shimpi",
            "major": "IT",
            "starting_year": 2022,
            "total_attendance": 14,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "300400":
        {
            "name": "Jigar Prajapati",
            "major": "CS",
            "starting_year": 2022,
            "total_attendance": 12,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "500800":
        {
            "name": "Shreyash Hassekar",
            "major": "AIDS",
            "starting_year": 2022,
            "total_attendance": 10,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        }

}

for key, value in data.items():
    ref.child(key).set(value)