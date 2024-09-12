# Automatic Attendance System (Face Recognition)

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.w8cgJkXfLSuZKmIf4UvjnQHaEQ%26pid%3DApi&f=1&ipt=8f4b6d9545b0c482d8a9239910ccd7e902cf161cca416f3b6d202cfde55b5063&ipo=images" alt="Face Recognition" align="center" loading="lazy">


## Working Principle
### 1. **Modules Imported:**
   - `face_recognition`: Used for detecting and encoding faces.
   - `cv2` (OpenCV): For capturing video and displaying the results.
   - `numpy`: For numerical operations.
   - `csv`: To write the attendance logs into a CSV file.
   - `datetime`: To get the current date and time for logging.

### 2. **Camera Initialization:**
   - The camera is initialized using OpenCV (`cv2.VideoCapture(camera)`), where the default camera is set to `0`. If an external camera is used, you can change this value.

### 3. **Loading and Encoding Known Faces:**
   - Several face images (e.g., A, Surjith, Ramprasath, etc.) are loaded using `face_recognition.load_image_file()`.
   - The faces are encoded using `face_recognition.face_encodings()` and stored in a list `known_face_encoding` for later comparison.

### 4. **Known Names:**
   - The names corresponding to the known face encodings are stored in a list `known_faces`. These names are used to identify people when their faces are detected.

### 5. **Attendance Logging:**
   - A CSV file is created with the current date (`data/YYYY-MM-DD.csv`) to log attendance.
   - The program writes the names and the time of detection into the CSV file.

### 6. **Face Detection and Recognition Loop:**
   - The script continuously captures frames from the camera feed.
   - Each frame is resized to 25% of its original size for faster face detection.
   - The frame is converted to RGB since `face_recognition` works with RGB images.
   - Face locations and encodings are extracted from the frame.
   - Each detected face is compared against the known faces using `face_recognition.compare_faces()` and `face_recognition.face_distance()`. The closest match is selected.
   - If the face matches a known person, the name is displayed on the video frame, and their attendance is logged.
   - If the face is not recognized, it is marked as "Unknown Person".

### 7. **Display and Exit:**
   - The script displays the video feed in a window labeled "Attendance System". If a known face is detected, it displays the name along with "Present"; otherwise, it shows "Unknown Person".
   - The loop continues until the user presses the "q" key, at which point the video capture is released, and the window is closed.


### Key Features:
- **Face Matching**: Recognizes and matches faces in real-time.
- **Attendance Logging**: Logs the name and the time of appearance in a CSV file.
- **Efficient Face Detection**: Uses downscaled frames to improve performance without compromising recognition accuracy.


[ins]: ./Installation.md
[pyn]: https://www.python.org/downloads/release/python-31011/
[pip]: https://pypi.org/project/pip/
[vsc]: https://code.visualstudio.com/download/
[pyc]: https://www.jetbrains.com/pycharm/download/


## For Installation Process:
- Refer the [Installation.md][ins] file.


## Note:
- Use the [Python 3.10][pyn] version.
- **Recommended Python Series** for the Execution.


## Tools:

| Tools   | Version       | Check |
|---------|---------------|-------|
| Python  | [3.10][pyn]   | [✔]   |
| Pip     | [latest][pip] | [✔]   |
| VSCode  | [latest][vsc] | [✔]   |
| PyCharm | [latest][pyc] | [✔]   |
