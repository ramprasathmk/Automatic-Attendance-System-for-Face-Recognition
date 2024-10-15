# Import the required modules here!
import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

# Initializing the Camera
"""
/**
 * Default value for `camera` is 0.
 *   camera = 0
 * If any other external camera or web-cam is connected
 *   Then set the " camera = 1 "
 */
"""
camera = 0  # default value is 0.
video_capture = cv2.VideoCapture(camera)

# declaring variable for `unrecognized` face of the person
unknown_name = ""

# Loading the image files in `name_image` variable
# and storing the encoded image files in the `name_encoding` variable.
tamil_image = face_recognition.load_image_file("photos/tamil.jpg")
tamil_image = cv2.cvtColor(tamil_image, cv2.COLOR_BGR2RGB)
tamil_encoding = face_recognition.face_encodings(tamil_image)[0]

muzamil_image = face_recognition.load_image_file("photos/muzamil.jpg")
muzamil_image = cv2.cvtColor(muzamil_image, cv2.COLOR_BGR2RGB)
muzamil_encoding = face_recognition.face_encodings(muzamil_image)[0]

surjith_image = face_recognition.load_image_file("photos/surjith.jpg")
surjith_image = cv2.cvtColor(surjith_image, cv2.COLOR_BGR2RGB)
surjith_encoding = face_recognition.face_encodings(surjith_image)[0]

ram_image = face_recognition.load_image_file("photos/ramp.jpg")
ram_image = cv2.cvtColor(ram_image, cv2.COLOR_BGR2RGB)
ram_encoding = face_recognition.face_encodings(ram_image)[0]

naveen_image = face_recognition.load_image_file("photos/naveen.jpg")
naveen_image = cv2.cvtColor(naveen_image, cv2.COLOR_BGR2RGB)
naveen_encoding = face_recognition.face_encodings(naveen_image)[0]

vasanth_image = face_recognition.load_image_file("photos/vasanth.jpg")
vasanth_image = cv2.cvtColor(vasanth_image, cv2.COLOR_BGR2RGB)
vasanth_encoding = face_recognition.face_encodings(vasanth_image)[0]

srini_image = face_recognition.load_image_file("photos/srini.jpg")
srini_image = cv2.cvtColor(srini_image, cv2.COLOR_BGR2RGB)
srini_encoding = face_recognition.face_encodings(srini_image)[0]

#  Add the encoded image variable in the `known_face_encoding` list.
known_face_encoding = [
    tamil_encoding,
    muzamil_encoding,
    surjith_encoding,
    ram_encoding,
    naveen_encoding,                                                                                         
    vasanth_encoding,
    srini_encoding
]

#  Loading the known faces names
known_faces = [
    "Tamil",
    "Muzamil",
    "Surjith", "Ramprasath", "Naveen", 
    "Vasanth", "Srini"
]

unknown_faces_names = []

#  Copying the know person faces to check their faces in the loop to detect their appearance.
students = known_faces.copy()

face_locations = []
face_encodings = []
face_names = []
recognize = True

# Set current date and time using `datetime` module.
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

with open(f"data/{current_date}.csv", "a", newline="") as f:
    #  Writing the person `Name` and `Time Appeared` data in the csv file.
    lnwriter = csv.writer(f)

    #  Beginning of the Loop
    try:
        while True:
            # `_` refers the index of the video_capture
            # `frame` refers the API Preference of the video_capture
            _, frame = video_capture.read()
            # Set the frame size
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # if your system takes the reverse of rgb encoding use this
            # rgb_small_frame = small_frame[:, :, :: -1] ## Default Value
            # rgb_small_frame = small_frame[:, :, :: 1] ## My Value
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

            # recognize the face and their encodings
            if recognize:
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(
                    rgb_small_frame, face_locations
                )
                face_names = []
                fontScale = 1.5
                thickness = 3
                lineType = 2

                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
                    name = ""
                    face_distance = face_recognition.face_distance(
                        known_face_encoding, face_encoding
                    )
                    best_match_index = np.argmin(face_distance)
                    if matches[best_match_index]:
                        name = known_faces[best_match_index]

                    face_names.append(name)
                    bottomLeftCornerOfText = (10, 100)
                    # if name and face matches
                    # do this
                    if name in known_faces:
                        font = cv2.FONT_ITALIC
                        fontColor = (4, 224, 107)
                        cv2.putText(
                            frame,
                            f"{name} Present",
                            bottomLeftCornerOfText,
                            font,
                            fontScale,
                            fontColor,
                            thickness,
                            lineType,
                        )

                        if name in students:
                            students.remove(name)
                            print(students)
                            current_time = now.strftime("%H-%M-%S")
                            lnwriter.writerow([name, current_time])

                    else:
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        fontColor = (252, 3, 3)
                        cv2.putText(
                            frame,
                            f"{unknown_name}Unknown Person",
                            bottomLeftCornerOfText,
                            font,
                            fontScale,
                            fontColor,
                            thickness,
                            lineType,
                        )

            cv2.imshow("Attendance System", frame)
            # ord("q") = 113
            if cv2.waitKey(1) & 0xFF == ord("q"):  # press q to exit.
                break  # destroy the process

    except KeyboardInterrupt as kie:
        print(kie)
    finally:
        print("Process Finished Successfully")

    video_capture.release()  # stop the video capture
    cv2.destroyAllWindows()  # destroy the cv2 frame
