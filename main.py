import cv2
from deepface import DeepFace
import pandas as pd
import numpy as np
import pickle
from datetime import datetime

# ------------------- LOAD ENCODINGS -------------------
with open("encodings.pkl", "rb") as f:
    data = pickle.load(f)

known_encodings = data["encodings"]
known_names = data["names"]

# To avoid marking the same person repeatedly
marked = set()

# ------------------- MARK ATTENDANCE -------------------
def mark_attendance(name):
    file_path = r"C:\Users\Darshan\FaceAttendance\attendance.csv"

    df = pd.read_csv(file_path)

    now = datetime.now()
    df.loc[len(df)] = [
        name,
        now.strftime("%Y-%m-%d"),
        now.strftime("%H:%M:%S")
    ]

    df.to_csv(file_path, index=False)
    print("Attendance written:", name)

# ------------------- START CAMERA -------------------
cap = cv2.VideoCapture(0)

print("Camera started... Press CTRL + C to stop.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    try:
        # Detect face and extract embedding
        result = DeepFace.represent(
            img_path=frame,
            model_name="Facenet",
            enforce_detection=False      # prevents errors
        )
    except Exception as e:
        print("Detection error:", e)
        continue

    if result is None or len(result) == 0:
        print("No face detected")
        continue

    embedding = np.array(result[0]["embedding"])

    # ------------------- COMPARE WITH KNOWN ENCODINGS -------------------
    best_match_name = "Unknown"
    best_similarity = 0

    for known_emb, name in zip(known_encodings, known_names):
        similarity = np.dot(known_emb, embedding) / (
            np.linalg.norm(known_emb) * np.linalg.norm(embedding)
        )

        if similarity > best_similarity:
            best_similarity = similarity
            best_match_name = name

    print("Similarity score:", best_similarity)

    # ------------------- THRESHOLD -------------------
    if best_similarity > 0.63:   # adjust if needed
        print("Recognized as:", best_match_name)

        # mark attendance only once
        if best_match_name not in marked:
            mark_attendance(best_match_name)
            marked.add(best_match_name)

        # draw box & name
        cv2.putText(frame, best_match_name, (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        print("Unknown face")
        cv2.putText(frame, "Unknown", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Face Recognition Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
