# Face Recognition Attendance System

A real-time attendance system built using **Python**, **OpenCV**, and **DeepFace**.  
This project detects faces through a webcam, recognizes the person, and automatically records attendance into a CSV file.

---

## 🚀 Features

- Real-time face detection  
- High-accuracy face recognition  
- Automatic attendance marking  
- Duplicate entry protection  
- Simple folder-based dataset  
- Easy to extend with more users  

---

## 📂 Project Structure

```

FaceAttendance/
│── Images/
│   └── Darshan/
│         └── 1.jpg
│
│── encode_faces.py
│── main.py
│── attendance.csv
│── encodings.pkl
│── requirements.txt
│── venv/
│── README.md

```

⚠️ **Folder names must NOT contain spaces.**  
Example: `Darshan`, `Rahul`, `ManjuKR`, `OmkarReddy`.

---

## 🧠 Requirements

Install all project dependencies using:

```

pip install -r requirements.txt

```

Or manually:

```

pip install deepface opencv-python numpy pandas tf-keras

```

---

## 🏗️ Setup Instructions

### 📌 Step 1 — Activate Virtual Environment

Go to project folder:

```

cd C:\Users\Darshan\FaceAttendance

```

Activate venv (PowerShell):

```

.\venv\Scripts\Activate.ps1

```

Or CMD:

```

venv\Scripts\activate

```

---

## 📸 Step 2 — Add Face Images

Inside the **Images** folder:

- Create one folder per person  
- Add at least one clear front face image  
- Image name must be `1.jpg` (or similar)  

Example:

```

Images/Darshan/1.jpg

```

---

## 🧬 Step 3 — Encode Faces

Run the script to generate `encodings.pkl`:

```

python encode_faces.py

```

You should see:

```

Face encoding completed!

```

---

## 🎥 Step 4 — Run Attendance System

Start webcam recognition:

```

python main.py

```

Press **q** anytime to quit.

If recognized:

```

Recognition: Darshan
Attendance written: Darshan

```

---

## 📄 Attendance Output

Attendance is stored in:

```

attendance.csv

```

Format:

```

Name,Date,Time
Darshan,2025-11-15,14:22:10

```

---

## ⚙️ How the System Works

1. **DeepFace** extracts a 128D embedding using Facenet  
2. Webcam captures live frames  
3. Embedding similarity is computed  
4. If similarity > threshold → recognized  
5. Attendance is written once per person  

---

## 🛠️ Troubleshooting

### ❌ Face not detected
- Use bright, clear face images  
- No mask, cap, or side-angle photos  

### ❌ Wrong person detected
Increase threshold in `main.py`:

```

if best_similarity > 0.65:

```

Try values: `0.67` or `0.70`

### ❌ Attendance not updating
Make sure file path is correct:

```

C:\Users\Darshan\FaceAttendance\attendance.csv

```

---

## 🎉 Project Ready!

You now have a fully working **Face Recognition Attendance System**.

If you want:
- A one-click `.bat` launcher  
- A GUI version  
- A mobile app version  
- A database upgrade  

Just tell me — I’ll build it for you.

---

## 👤 Author

**Darshan Naik**  
– Engineering Final Year

