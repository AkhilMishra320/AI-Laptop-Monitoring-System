import face_recognition
import os
import cv2
import numpy as np


class FaceRecognizer:
    def __init__(self, known_faces_dir="data/known_faces"):
        self.known_encodings = []
        self.known_names = []

        if not os.path.exists(known_faces_dir):
            print("Known faces directory not found!")
            return

        for filename in os.listdir(known_faces_dir):
            path = os.path.join(known_faces_dir, filename)

            # Skip non-image files
            if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
                continue

            print(f"Processing: {filename}")

            # --- SAFE IMAGE LOAD ---
            image = cv2.imread(path, cv2.IMREAD_COLOR)

            if image is None:
                print(f"Failed to load {filename}")
                continue

            # Ensure 3 channels
            if len(image.shape) != 3:
                print(f"Invalid image shape in {filename}")
                continue

            # Convert BGR → RGB
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Force uint8 (important)
            if image.dtype != np.uint8:
                image = image.astype(np.uint8)

            # Final safety check
            if image.ndim != 3 or image.shape[2] != 3:
                print(f"Image not valid RGB in {filename}")
                continue

            try:
                encodings = face_recognition.face_encodings(image)
            except Exception as e:
                print(f"Encoding error in {filename}: {e}")
                continue

            if len(encodings) > 0:
                self.known_encodings.append(encodings[0])
                name = os.path.splitext(filename)[0]
                self.known_names.append(name)
                print(f"{name} loaded successfully")
            else:
                print(f"No face found in {filename}")

        print("Total faces loaded:", len(self.known_encodings))

    def recognize(self, frame):
        # Safety: ensure frame valid
        if frame is None:
            return [], []

        if frame.dtype != np.uint8:
            frame = frame.astype(np.uint8)

        # Convert BGR → RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        names = []

        for face_encoding in face_encodings:
            name = "Unknown"

            if len(self.known_encodings) > 0:
                matches = face_recognition.compare_faces(
                    self.known_encodings,
                    face_encoding
                )

                if True in matches:
                    first_match_index = matches.index(True)
                    name = self.known_names[first_match_index]

            names.append(name)

        return face_locations, names