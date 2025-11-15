# 🚀 Face Recognition Attendance System

### Real-Time Face Detection • Deep Learning • Automated Attendance

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge" /> 
  <img src="https://img.shields.io/badge/OpenCV-Live%20Detection-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/DeepFace-FaceNet-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
</p>

A powerful **AI-based Attendance Monitoring System** that uses **DeepFace (FaceNet model)** to recognize faces in real-time and log attendance automatically with timestamps.

---

## ✨ Key Features

✔ Real-time webcam-based face detection
✔ High-accuracy recognition using **Facenet embeddings**
✔ Automatic attendance recording (Name, Date, Time)
✔ Prevents duplicate entries
✔ Easy to add new users (just upload images)
✔ Clean, modular, scalable codebase

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

---

## 🛠️ Tech Stack

| Component            | Technology                |
| -------------------- | ------------------------- |
| Face Detection       | DeepFace + RetinaFace     |
| Face Recognition     | Facenet Embeddings        |
| Programming Language | Python 3.10               |
| Computer Vision      | OpenCV                    |
| Data Storage         | CSV                       |
| ML Libraries         | TensorFlow, NumPy, Pandas |

---

## 📸 Add User Images

To register a person:

```
Images/<PersonName>/1.jpg
```

**Important:**

* Folder names **must NOT contain spaces**
* Image must clearly show the face

Example:

```
Images/Darshan/1.jpg
```

Add more users the same way.

---

## ⚙️ Setup Instructions

### **1️⃣ Activate Virtual Environment**

```
cd C:\Users\Darshan\FaceAttendance
.\venv\Scripts\Activate.ps1
```

---

### **2️⃣ Install Dependencies**

```
pip install -r requirements.txt
```

Or manually:

```
pip install deepface opencv-python numpy pandas tf-keras
```

---

### **3️⃣ Generate Face Encodings**

```
python encode_faces.py
```

Expected:

```
Face encoding completed!
```

This creates:

```
encodings.pkl
```

---

### **4️⃣ Start Attendance System**

```
python main.py
```

📌 Press **Q** to quit.

---

## 📄 Attendance Output

All attendance entries are stored in:

```
attendance.csv
```

Format:

```
Name,Date,Time
Darshan,2025-11-15,14:22:10
```

---

## 🧠 How It Works (Flow)

1. Images → Encoded into 128-D embeddings (Facenet)
2. Webcam feed → Face detected using RetinaFace
3. Embedding extracted from live frame
4. Compare similarity with stored encodings
5. If score > threshold → recognized
6. Attendance logged in CSV

---

## 🛠️ Troubleshooting

### ❌ Face not detected

* Ensure good lighting
* Use a clear, front-facing photo
* Avoid blur, side angles, masks

### ❌ Wrong person recognized

Increase matching threshold:

In `main.py`, modify:

```
if best_similarity > 0.65:
```

Try: **0.67 / 0.70 / 0.75**

### ❌ Attendance not updating

Be sure path is correct:

```
C:\Users\Darshan\FaceAttendance\attendance.csv
```

---

## 📌 Future Enhancements

* Web dashboard (Streamlit / Flask)
* Live face registration
* Cloud sync (Firebase / MongoDB)
* Mobile app integration
* Email/SMS notifications
* Accuracy boost using ArcFace

---

## 👤 Author

**Darshan Naik**
Full Stack / ML Engineer

