# import dlib
# import cv2

# # Model ka path set karein
# predictor_path = "models/shape_predictor_68_face_landmarks.dat"

# # Dlib ke tools initialize karein
# detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor(predictor_path)

# def get_eye_status(frame):
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = detector(gray)
    
#     for face in faces:
#         landmarks = predictor(gray, face)
        
#         # Example: Left eye ke coordinates nikalna
#         left_eye_x = landmarks.part(36).x 
#         left_eye_y = landmarks.part(36).y
        
#         # Yahan hum logic lagayenge ki "Looking" ya "Not Looking"
#         return "Looking"
    
#     return "No Face"





# import cv2
# import dlib
# import numpy as np

# # Model Path (Jo tumne models folder mein rakha hai)
# PREDICTOR_PATH = "models/shape_predictor_68_face_landmarks.dat"

# # Dlib initialize karein
# detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor(PREDICTOR_PATH)

# def get_eye_status(frame):
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = detector(gray)
    
#     if len(faces) == 0:
#         return "NO FACE", (255, 255, 255) # White color

#     for face in faces:
#         landmarks = predictor(gray, face)
        
#         # Eye Points (Dlib Indexing)
#         # Left Eye: 36 to 41 | Right Eye: 42 to 47
        
#         # Simple Logic: Agar face ka center frame ke center se bahut door hai
#         # toh user side mein dekh raha hai.
        
#         face_center_x = face.center().x
#         frame_center_x = frame.shape[1] // 2
        
#         # Tolerance: 100 pixels ka gap allow hai
#         if abs(face_center_x - frame_center_x) > 100:
#             return "NOT LOOKING", (0, 255, 255) # Yellow color
        
#         # Yahan hum landmarks bhi draw kar sakte hain debugging ke liye
#         # for n in range(36, 48):
#         #     x = landmarks.part(n).x
#         #     y = landmarks.part(n).y
#         #     cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

#     return "LOOKING", (0, 255, 0) # Green color


#**********************************************************

import cv2
import dlib
import numpy as np
import time
import os

# Model Path
PREDICTOR_PATH = "models/shape_predictor_68_face_landmarks.dat"

# Dlib initialize
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(PREDICTOR_PATH)

# Timer variables
start_time = None
BUFFER_TIME = 300  # 5 minutes in seconds

def get_eye_status(frame):
    global start_time
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    
    # 1. Agar face nahi dikha ya user screen ki taraf nahi dekh raha
    status = "LOOKING"
    color = (0, 255, 0)
    
    looking_at_screen = False

    if len(faces) > 0:
        for face in faces:
            # Face center logic
            face_center_x = face.center().x
            frame_center_x = frame.shape[1] // 2
            
            if abs(face_center_x - frame_center_x) <= 150: # Thoda tolerance badha diya hai camera quality ke liye
                looking_at_screen = True
                break

    # 2. Timer Logic
    if not looking_at_screen:
        if start_time is None:
            start_time = time.time() # Timer shuru karo
        
        elapsed_time = int(time.time() - start_time)
        remaining_time = BUFFER_TIME - elapsed_time
        
        status = f"NOT LOOKING ({remaining_time}s left)"
        color = (0, 0, 255) # Red color for warning

        # 3. Agar 5 min pure ho gaye toh SLEEP karo
        if elapsed_time >= BUFFER_TIME:
            print("User not detected for 5 mins. Putting laptop to sleep...")
            # Windows Sleep Command
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            start_time = None # Reset timer after sleep
            
    else:
        # Agar user wapas aa gaya, toh timer reset kar do
        start_time = None
        status = "LOOKING"
        color = (0, 255, 0)

    return status, color