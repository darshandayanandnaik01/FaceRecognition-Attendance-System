from deepface import DeepFace
import os
import pickle

def encode_faces():
    encodings = []
    names = []

    base_path = "Images"
    for person in os.listdir(base_path):
        person_path = os.path.join(base_path, person)
        for img_name in os.listdir(person_path):
            img_path = os.path.join(person_path, img_name)

            embedding = DeepFace.represent(img_path=img_path, model_name="Facenet")[0]["embedding"]

            encodings.append(embedding)
            names.append(person)

    with open("encodings.pkl", "wb") as f:
        pickle.dump({"encodings": encodings, "names": names}, f)

    print("Face encoding completed!")

if __name__ == "__main__":
    encode_faces()
