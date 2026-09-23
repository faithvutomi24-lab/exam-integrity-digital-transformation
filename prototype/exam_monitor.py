import cv2
import os
import time
from datetime import datetime

# --------------------------------------------------
# EXAM INTEGRITY MONITORING PROTOTYPE
# --------------------------------------------------

# Find the face detection file
file_path = os.path.join(
    os.path.dirname(__file__),
    "haarcascade_frontalface_default.xml"
)

# Load the face detector
face_detector = cv2.CascadeClassifier(file_path)

if face_detector.empty():
    print("ERROR: Face detector could not be loaded.")
    print("Make sure haarcascade_frontalface_default.xml is in this folder.")
    exit()

print("Face detector loaded successfully.")

# Open the webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("ERROR: Could not access the webcam.")
    exit()

# --------------------------------------------------
# SESSION INFORMATION
# --------------------------------------------------

start_time = time.time()

# Count unusual incidents
incident_count = 0

# Remember the previous situation
previous_status = "Face detected"

# Store event history
event_log = []

# Flag threshold
FLAG_THRESHOLD = 3

print("Exam monitoring session started.")
print("Press Q to end the session.")

# --------------------------------------------------
# MAIN MONITORING LOOP
# --------------------------------------------------

while True:

    success, frame = camera.read()

    if not success:
        print("Could not read from webcam.")
        break

    # Convert image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    # Count faces
    face_count = len(faces)

    # --------------------------------------------------
    # DETERMINE CURRENT STATUS
    # --------------------------------------------------

    if face_count == 1:

        current_status = "Face detected"

    elif face_count == 0:

        current_status = "No face detected"

    else:

        current_status = "Multiple faces detected"

    # --------------------------------------------------
    # COUNT A NEW INCIDENT ONLY WHEN STATUS CHANGES
    # --------------------------------------------------

    if current_status != previous_status:

        if current_status != "Face detected":

            incident_count += 1

            event_time = datetime.now().strftime("%H:%M:%S")

            event_log.append(
                f"{event_time} - {current_status}"
            )

    previous_status = current_status

    # --------------------------------------------------
    # HUMAN REVIEW FLAG
    # --------------------------------------------------

    if incident_count >= FLAG_THRESHOLD:

        display_status = "FLAGGED FOR HUMAN REVIEW"

    else:

        display_status = current_status

    # --------------------------------------------------
    # DISPLAY STATUS
    # --------------------------------------------------

    cv2.putText(
        frame,
        display_status,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 255, 0),
        2
    )

    # Display incident count
    cv2.putText(
        frame,
        "Unusual incidents: " + str(incident_count),
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    # Display number of faces
    cv2.putText(
        frame,
        "Faces detected: " + str(face_count),
        (20, 115),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    # --------------------------------------------------
    # DRAW FACE BOXES
    # --------------------------------------------------

    for (x, y, width, height) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + width, y + height),
            (255, 0, 0),
            2
        )

    # --------------------------------------------------
    # DISPLAY THE MONITORING WINDOW
    # --------------------------------------------------

    cv2.imshow(
        "Exam Integrity Monitoring Prototype",
        frame
    )

    # Press Q to end the exam
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# --------------------------------------------------
# END SESSION
# --------------------------------------------------

end_time = time.time()

session_duration = end_time - start_time

minutes = int(session_duration // 60)
seconds = int(session_duration % 60)

# Close webcam
camera.release()
cv2.destroyAllWindows()

# --------------------------------------------------
# DISPLAY FINAL REPORT
# --------------------------------------------------

print("\n----------------------------------------")
print("EXAM MONITORING SESSION SUMMARY")
print("----------------------------------------")

print(
    f"Session duration: {minutes} minutes {seconds} seconds"
)

print(
    f"Unusual incidents: {incident_count}"
)

if incident_count >= FLAG_THRESHOLD:

    print("Final status: FLAGGED FOR HUMAN REVIEW")

else:

    print("Final status: NO REVIEW FLAG")

print("\nEvent log:")

if len(event_log) == 0:

    print("No unusual events recorded.")

else:

    for event in event_log:

        print(event)

print("----------------------------------------")
print("Session ended.")
