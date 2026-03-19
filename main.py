# import cv2
# from modules.face_recognize import FaceRecognizer

# def main():
#     cap = cv2.VideoCapture(0)

#     if not cap.isOpened():
#         print("Camera open nahi ho raha")
#         return

#     recognizer = FaceRecognizer()

#     print("Day 3: Face Recognition Running")

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         frame = cv2.flip(frame, 1)

#         face_locations, names = recognizer.recognize(frame)

#         for (top, right, bottom, left), name in zip(face_locations, names):
#             cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
#             cv2.putText(frame, name, (left, top - 10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

#         cv2.imshow("Face Recognition", frame)

#         key = cv2.waitKey(1) & 0xFF
#         if key == 27:
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()


###################################
### 2️⃣ File: `main.py`


# import cv2
# import face_recognition
# import time
# import os
# from modules.security_actions import save_intruder_screenshot

# # 1. Setup: Akhil ki photo ka rasta
# KNOWN_FACE_PATH = "data/known_faces/akhil1.jpg"

# if not os.path.exists(KNOWN_FACE_PATH):
#     print(f"❌ Error: {KNOWN_FACE_PATH} nahi mili! Photo pehle dalo.")
#     exit()

# print("AI System Booting... Loading Akhil's Face")
# akhil_image = face_recognition.load_image_file(KNOWN_FACE_PATH)
# akhil_encoding = face_recognition.face_encodings(akhil_image)[0]

# # 2. Camera Start
# cap = cv2.VideoCapture(0)
# unknown_timer_start = None

# print("🛡️ Security Guard is LIVE. Press 'q' to stop.")

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Speed badhane ke liye frame resize karein
#     small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#     rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

#     # Chehra dhundo aur pehchano
#     face_locations = face_recognition.face_locations(rgb_small_frame)
#     face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#     is_akhil_present = False

#     for encoding in face_encodings:
#         matches = face_recognition.compare_faces([akhil_encoding], encoding)
#         if matches[0]:
#             is_akhil_present = True
#             break

#     # 3. Decision Logic
#     if is_akhil_present:
#         unknown_timer_start = None # Timer reset kyunki Akhil mil gaya
#         status_text = "WELCOME AKHIL"
#         color = (0, 255, 0) # Green color
#     else:
#         if unknown_timer_start is None:
#             unknown_timer_start = time.time()
        
#         time_elapsed = time.time() - unknown_timer_start
#         status_text = f"UNKNOWN! Screenshot in: {max(0, 3 - int(time_elapsed))}s"
#         color = (0, 0, 255) # Red color

#         # Agar 3 second tak koi unknown raha
#         if time_elapsed > 3:
#             save_intruder_screenshot(frame)
#             unknown_timer_start = time.time() # Reset taaki lagatar save na ho

#     # Screen pe text dikhao
#     cv2.putText(frame, status_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
#     cv2.imshow("Laptop Security Monitor", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

####################################



#*******************************************************
### 🛡️ Updated `main.py` (Final Smart Logic)

# import cv2
# import face_recognition
# import time
# import os
# from modules.security_actions import save_intruder_screenshot

# # --- SETUP ---
# # Akhil ki photo load ho rahi hai
# KNOWN_FACE_PATH = "data/known_faces/akhil1.jpg"
# akhil_image = face_recognition.load_image_file(KNOWN_FACE_PATH)
# akhil_encoding = face_recognition.face_encodings(akhil_image)[0]

# cap = cv2.VideoCapture(0)
# unknown_timer_start = None
# screenshot_done = False 

# print("🛡️ Guard Active: Jab tak Akhil hai, sab safe hai.")

# while True:
#     ret, frame = cap.read()
#     if not ret: break
#     frame = cv2.flip(frame, 1) 


#     # Performance ke liye image choti karein
#     small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#     rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

#     # Saare chehre dhundo jo camera ke samne hain
#     face_locations = face_recognition.face_locations(rgb_small_frame)
#     face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#     is_akhil_present = False

#     # Ek-ek karke saare chehro ko Akhil se match karo
#     for encoding in face_encodings:
#         match = face_recognition.compare_faces([akhil_encoding], encoding)
#         if match[0]:
#             is_akhil_present = True # Akhil mil gaya!
#             break

#     # --- DECISION LOGIC ---
    
#     if is_akhil_present:
#         # AGAR AKHIL HAI: Sab maaf hai, photo mat lo
#         unknown_timer_start = None
#         screenshot_done = False 
#         status_text = "AKHIL PRESENT - SYSTEM SAFE"
#         color = (0, 255, 0) # Green
    
#     elif len(face_encodings) > 0:
#          # AKHIL NAHI HAI: Lekin koi aur chehra dikh raha hai
#          if unknown_timer_start is None:
#              unknown_timer_start = time.time()
        
#          time_elapsed = time.time() - unknown_timer_start
        
#          if screenshot_done:
#              status_text = "INTRUDER LOGGED"
#              color = (255, 0, 0) # Blue
#          else:
#              status_text = f"UNKNOWN USER! Alert in: {max(0, 3 - int(time_elapsed))}s"
#              color = (0, 0, 255) # Red

#              # 3 second baad screenshot
#              if time_elapsed > 3:
#                  save_intruder_screenshot(frame)
#                  screenshot_done = True
#     else:
#          # CAMERA KHALI HAI: Koi nahi dikh raha
#          status_text = "NO FACE DETECTED"
#          color = (255, 255, 255) # White
#          unknown_timer_start = None

#     # Screen pe text likho
#     cv2.putText(frame, status_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
#     cv2.imshow("Akhil's Smart Monitor", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()



#***************************************************************************

# # 1. **Scenario A (Akhil + Dost):** Camera 2 chehre dekhega. System poochega "Kya koi Akhil hai?". Answer aayega "Haan". System shant rahega aur koi photo nahi lega.
# # 2. **Scenario B (Dost 1 + Dost 2):** Camera 2 chehre dekhega. System poochega "Kya koi Akhil hai?". Answer aayega "Nahi". System turant 3 second ka timer chalayega aur photo khinch lega.
# # 3. **Scenario C (Dost akela):** Akhil nahi hai, toh photo khinch jayegi.

# # **Testing Tip:** Apne laptop ke samne apne kisi dost ki photo dikhao (phone mein) aur khud hat jao. Check karo ki kya wo screenshot le raha hai. Phir khud samne aao aur dekho ki kya wo screenshot lena band kar deta hai.

# # **Ab check karke batao Akhil, kya logic sahi kaam kar raha hai? Iske baad hum direct Gmail setup karenge.**


########################################################3


### Updated `main.py`


# import cv2
# import face_recognition
# import time
# import os
# import numpy as np
# from modules.security_actions import save_intruder_screenshot

# # Setup
# KNOWN_FACE_PATH = "data/known_faces/akhil1.jpg"
# akhil_image = face_recognition.load_image_file(KNOWN_FACE_PATH)
# akhil_encoding = face_recognition.face_encodings(akhil_image)[0]

# cap = cv2.VideoCapture(0)
# unknown_timer_start = None
# screenshot_done = False 

# print("🛡️ Mirror Fixed & Circular Preview Active.")

# while True:
#     ret, frame = cap.read()
#     if not ret: break

#     # --- 1. MIRROR FIX (Left-Right Swap Fix) ---
#     frame = cv2.flip(frame, 1) 

#     # --- 2. CIRCULAR PREVIEW LOGIC ---
#     # Ek black image banaiye frame ke size ki
#     mask = np.zeros(frame.shape, dtype=np.uint8)
#     # Circle ka center aur size (Yahan radius set kar sakte ho)
#     center = (frame.shape[1] - 100, 80) # Top-right corner mein
#     radius = 70 
#     # Mask pe white circle draw karein
#     cv2.circle(mask, center, radius, (255, 255, 255), -1)
#     # Original frame aur mask ko merge karein
#     circular_preview = cv2.bitwise_and(frame, mask)

#     # Performance ke liye processing
#     small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#     rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

#     face_locations = face_recognition.face_locations(rgb_small_frame)
#     face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#     is_akhil_present = False
#     for encoding in face_encodings:
#         match = face_recognition.compare_faces([akhil_encoding], encoding)
#         if match[0]:
#             is_akhil_present = True
#             break

#     # Decision Logic
#     if is_akhil_present:
#         unknown_timer_start = None
#         screenshot_done = False 
#         status_text = "AKHIL OK"
#         color = (0, 255, 0)
#     elif len(face_encodings) > 0:
#         if unknown_timer_start is None:
#             unknown_timer_start = time.time()
        
#         time_elapsed = time.time() - unknown_timer_start
#         status_text = "UNKNOWN!"
#         color = (0, 0, 255)

#         if time_elapsed > 3 and not screenshot_done:
#             save_intruder_screenshot(frame)
#             screenshot_done = True
#     else:
#         status_text = "SCANNING..."
#         color = (255, 255, 255)

#     # UI Display (Circle ke niche text)
#     cv2.putText(frame, status_text, (frame.shape[1]-160, 170), 
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
    
#     # Sirf circle wala hissa dikhane ke liye (Optional: pure frame ki jagah sirf circle)
#     # Hum background ko thoda dark kar dete hain taaki circle highlight ho
#     final_output = cv2.addWeighted(frame, 0.2, circular_preview, 0.8, 0)

#     cv2.imshow("Smart Security Monitor", final_output)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()





# import cv2
# import face_recognition
# import time
# import os
# from modules.security_actions import save_intruder_screenshot

# # --- SETUP ---
# # Akhil ki photo load ho rahi hai
# KNOWN_FACE_PATH = "data/known_faces/akhil1.jpg"
# akhil_image = face_recognition.load_image_file(KNOWN_FACE_PATH)
# akhil_encoding = face_recognition.face_encodings(akhil_image)[0]

# cap = cv2.VideoCapture(0)
# unknown_timer_start = None
# screenshot_done = False 

# print("🛡️ Guard Active: Jab tak Akhil hai, sab safe hai.")

# while True:
#     ret, frame = cap.read()
#     if not ret: break
#     frame = cv2.flip(frame, 1) 


#     # Performance ke liye image choti karein
#     small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#     rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

#     # Saare chehre dhundo jo camera ke samne hain
#     face_locations = face_recognition.face_locations(rgb_small_frame)
#     face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#     is_akhil_present = False

#     # Ek-ek karke saare chehro ko Akhil se match karo
#     for encoding in face_encodings:
#         match = face_recognition.compare_faces([akhil_encoding], encoding)
#         if match[0]:
#             is_akhil_present = True # Akhil mil gaya!
#             break

#     # --- DECISION LOGIC ---
    
#     if is_akhil_present:
#         # AGAR AKHIL HAI: Sab maaf hai, photo mat lo
#         unknown_timer_start = None
#         screenshot_done = False 
#         status_text = "AKHIL PRESENT - SYSTEM SAFE"
#         color = (0, 255, 0) # Green
    
#     elif len(face_encodings) > 0:
#          # AKHIL NAHI HAI: Lekin koi aur chehra dikh raha hai
#          if unknown_timer_start is None:
#              unknown_timer_start = time.time()
        
#          time_elapsed = time.time() - unknown_timer_start
        
#          if screenshot_done:
#              status_text = "INTRUDER LOGGED"
#              color = (255, 0, 0) # Blue
#          else:
#              status_text = f"UNKNOWN USER! Alert in: {max(0, 3 - int(time_elapsed))}s"
#              color = (0, 0, 255) # Red

#              # 3 second baad screenshot
#              if time_elapsed > 3:
#                  save_intruder_screenshot(frame)
#                  screenshot_done = True
#     else:
#          # CAMERA KHALI HAI: Koi nahi dikh raha
#          status_text = "NO FACE DETECTED"
#          color = (255, 255, 255) # White
#          unknown_timer_start = None

#     # Screen pe text likho
#     cv2.putText(frame, status_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
#     cv2.imshow("Akhil's Smart Monitor", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()



#*********************************

# import cv2
# import face_recognition
# import time
# import os
# # Humare modules import kar rahe hain
# from modules.security_actions import save_intruder_screenshot
# from modules.eye_tracking import get_eye_status 

# # --- SETUP ---
# # Akhil ki photo load ho rahi hai
# KNOWN_FACE_PATH = "data/known_faces/akhil1.jpg"
# akhil_image = face_recognition.load_image_file(KNOWN_FACE_PATH)
# akhil_encoding = face_recognition.face_encodings(akhil_image)[0]

# cap = cv2.VideoCapture(0)
# unknown_timer_start = None
# screenshot_done = False 

# print("🛡️ Guard Active: System scanning for Akhil...")

# while True:
#     ret, frame = cap.read()
#     if not ret: break
    
#     # 1. NO MIRROR EFFECT: frame = cv2.flip(frame, 1) ko hata diya hai
#     # Ab screen natural dikhegi.

#     # Performance ke liye image choti karein
#     small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#     rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

#     # Face Detection
#     face_locations = face_recognition.face_locations(rgb_small_frame)
#     face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#     is_akhil_present = False
    
#     # --- STEP 1: FACE RECOGNITION (STRICT MODE) ---
#     for encoding in face_encodings:
#         # 0.4 Tolerance ka matlab hai 60% accuracy se match hona chahiye (Strict)
#         matches = face_recognition.compare_faces([akhil_encoding], encoding, tolerance=0.4)
        
#         if matches[0]:
#             is_akhil_present = True
#             break

#     # --- STEP 2: EYE TRACKING & LOGIC ---
#     if is_akhil_present:
#         # Agar Akhil hai, toh check karo wo screen par dekh raha hai ya nahi
#         eye_label, eye_color = get_eye_status(frame)
        
#         if eye_label == "LOOKING":
#             status_text = "AKHIL PRESENT - SYSTEM SAFE"
#             color = (0, 255, 0) # Green
#         else:
#             status_text = "EYE DISTRACTED - FOCUS PLEASE!"
#             color = (0, 255, 255) # Yellow (Warning)
            
#         unknown_timer_start = None
#         screenshot_done = False 
    
#     elif len(face_encodings) > 0:
#         # AKHIL NAHI HAI (Unknown Person like Pankaj)
#         if unknown_timer_start is None:
#             unknown_timer_start = time.time()
        
#         time_elapsed = time.time() - unknown_timer_start
        
#         if screenshot_done:
#             status_text = "INTRUDER LOGGED"
#             color = (255, 0, 0) # Blue
#         else:
#             status_text = f"UNKNOWN USER! Alert in: {max(0, 3 - int(time_elapsed))}s"
#             color = (0, 0, 255) # Red

#             # 3 second baad screenshot
#             if time_elapsed > 3:
#                 save_intruder_screenshot(frame)
#                 screenshot_done = True
#     else:
#         # CAMERA KHALI HAI
#         status_text = "NO FACE DETECTED"
#         color = (255, 255, 255) # White
#         unknown_timer_start = None

#     # --- STEP 3: VISUALS (RECTANGLE ONLY) ---
#     # Draw rectangles for all detected faces
#     for (top, right, bottom, left) in face_locations:
#         # Scale back up since we resized to 0.25
#         top *= 4; right *= 4; bottom *= 4; left *= 4
#         cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

#     # Screen pe status likho
#     cv2.putText(frame, status_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
#     cv2.imshow("Akhil's Smart Monitor", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()






### Kya Change Kiya?

# 1. **Variable Unpacking:** `get_eye_status(frame)` ab do cheezein bhej raha hai (text aur color), toh maine usey handle karne ke liye update kiya hai.
# 2. **Display Logic:** Agar aap screen par nahi dekh rahe hain, toh wo **"EYE DISTRACTED"** ke saath-saath timer (e.g., *290s left*) bhi dikhayega.
# 3. **Strict Coordination:** Jab Akhil present hai, tabhi eye tracking chale, warna intruder logic chale.

### Updated `main.py`


# import cv2
# import face_recognition
# import time
# import os
# # Humare modules import kar rahe hain
# from modules.security_actions import save_intruder_screenshot
# from modules.eye_tracking import get_eye_status 

# # --- SETUP ---
# KNOWN_FACE_PATH = "data/known_faces/akhil1.jpg"
# akhil_image = face_recognition.load_image_file(KNOWN_FACE_PATH)
# akhil_encoding = face_recognition.face_encodings(akhil_image)[0]

# cap = cv2.VideoCapture(0)
# unknown_timer_start = None
# screenshot_done = False 

# print("🛡️ Guard Active: System scanning for Akhil...")

# while True:
#     ret, frame = cap.read()
#     if not ret: break
#     frame = cv2.flip(frame, 1) 
    
#     # Performance ke liye image choti karein
#     small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#     rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

#     # Face Detection
#     face_locations = face_recognition.face_locations(rgb_small_frame)
#     face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#     is_akhil_present = False
    
#     # --- STEP 1: FACE RECOGNITION (STRICT MODE) ---
#     for encoding in face_encodings:
#         matches = face_recognition.compare_faces([akhil_encoding], encoding, tolerance=0.4)
#         if matches[0]:
#             is_akhil_present = True
#             break

#     # --- STEP 2: EYE TRACKING & LOGIC ---
#     if is_akhil_present:
#         # UPDATED: Ab ye eye_tracking se updated text aur color lega (Timer ke saath)
#         eye_label, eye_color = get_eye_status(frame)
        
#         if "LOOKING" in eye_label and "NOT" not in eye_label:
#             status_text = "AKHIL PRESENT - SYSTEM SAFE"
#             color = (0, 255, 0) # Green
#         else:
#             # Agar distracting hai toh wahi text dikhayega jo eye_tracking bhej raha hai (Timer)
#             status_text = f"FOCUS! {eye_label}"
#             color = eye_color # Red/Yellow from eye_tracking.py
            
#         unknown_timer_start = None
#         screenshot_done = False 
    
#     elif len(face_encodings) > 0:
#         # AKHIL NAHI HAI
#         if unknown_timer_start is None:
#             unknown_timer_start = time.time()
        
#         time_elapsed = time.time() - unknown_timer_start
        
#         if screenshot_done:
#             status_text = "INTRUDER LOGGED"
#             color = (255, 0, 0) 
#         else:
#             status_text = f"UNKNOWN USER! Alert in: {max(0, 3 - int(time_elapsed))}s"
#             color = (0, 0, 255) 

#             if time_elapsed > 3:
#                 save_intruder_screenshot(frame)
#                 screenshot_done = True
#     else:
#         # CAMERA KHALI HAI
#         # Yahan bhi eye status call karna zaroori hai taaki timer chalta rahe agar face chala jaye
#         eye_label, eye_color = get_eye_status(frame) 
#         status_text = f"NO FACE - {eye_label}"
#         color = (255, 255, 255)
#         unknown_timer_start = None

#     # --- STEP 3: VISUALS ---
#     for (top, right, bottom, left) in face_locations:
#         top *= 4; right *= 4; bottom *= 4; left *= 4
#         cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

#     # Screen pe status likho
#     cv2.putText(frame, status_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
#     cv2.imshow("Akhil's Smart Monitor", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()



### Ab Testing Kaise Karein?

# 1. **Step 1:** Pehle apne `modules/eye_tracking.py` mein `BUFFER_TIME = 300` ko badal kar **`BUFFER_TIME = 10`** kar dein.
# 2. **Step 2:** Code run karein aur camera se hat jayein ya aankhein band kar lein.
# 3. **Step 3:** Dekhiye ki screen par countdown (10s, 9s...) aa raha hai ya nahi.
# 4. **Step 4:** 10 second khatam hote hi check kijiye ki laptop **Sleep Mode** mein gaya ya nahi.

# ---

# **Next Step:** Kya aapka Gmail bhejane wala code (`security_actions.py`) ready hai? Agar nahi, toh kya main uske liye **SMTP logic** likh kar doon?




### Final `main.py`



# import cv2
# import face_recognition
# import time
# import os
# import numpy as np
# # Humare modules import kar rahe hain
# from modules.security_actions import save_intruder_screenshot
# from modules.eye_tracking import get_eye_status 

# # --- STEP 1: SMART SETUP (Multiple Photos Load Karein) ---
# known_face_encodings = []
# known_face_names = []
# faces_folder = "data/known_faces/"

# print("⌛ Loading all face angles for better accuracy...")

# # Check karein ki folder hai ya nahi
# if not os.path.exists(faces_folder):
#     os.makedirs(faces_folder)

# # Folder se har ek photo load karke uska encoding list banayein
# for file_name in os.listdir(faces_folder):
#     if file_name.endswith((".jpg", ".png", ".jpeg")):
#         img_path = os.path.join(faces_folder, file_name)
#         image = face_recognition.load_image_file(img_path)
#         encoding = face_recognition.face_encodings(image)
        
#         if len(encoding) > 0:
#             known_face_encodings.append(encoding[0])
#             known_face_names.append("Akhil")
#             print(f"✅ Loaded: {file_name}")

# if not known_face_encodings:
#     print("❌ ERROR: data/known_faces/ mein koi photo nahi mili! Pehle trainer.py chalayein.")
#     exit()

# # --- STEP 2: INITIALIZE ---
# cap = cv2.VideoCapture(0)
# unknown_timer_start = None
# screenshot_done = False 

# print("🛡️ Guard Active: System scanning for Akhil...")

# while True:
#     ret, frame = cap.read()
#     if not ret: break
#     frame = cv2.flip(frame, 1) 
    
#     # Optional: Camera ko natural dikhane ke liye flip karein
#     # frame = cv2.flip(frame, 1) 

#     # Performance ke liye image choti karein
#     small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#     rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

#     # Face Detection
#     face_locations = face_recognition.face_locations(rgb_small_frame)
#     face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#     is_akhil_present = False
    
#     # --- STEP 3: FACE MATCHING LOGIC ---
#     for encoding in face_encodings:
#         # Multiple encodings se match check karein
#         matches = face_recognition.compare_faces(known_face_encodings, encoding, tolerance=0.45)
        
#         if True in matches:
#             is_akhil_present = True
#             break

#     # --- STEP 4: EYE TRACKING & SECURITY LOGIC ---
#     if is_akhil_present:
#         # Eye tracking se status aur timer color lein
#         eye_label, eye_color = get_eye_status(frame)
        
#         if "LOOKING" in eye_label and "NOT" not in eye_label:
#             status_text = "AKHIL PRESENT - SYSTEM SAFE"
#             color = (0, 255, 0) # Green
#         else:
#             # Jab focus na ho toh eye_tracking.py ka timer dikhaye
#             status_text = f"ATTENTION! {eye_label}"
#             color = eye_color # Red/Yellow from eye_tracking.py
            
#         unknown_timer_start = None
#         screenshot_done = False 
    
#     elif len(face_encodings) > 0:
#         # UNKNOWN USER DETECTED
#         if unknown_timer_start is None:
#             unknown_timer_start = time.time()
        
#         time_elapsed = time.time() - unknown_timer_start
        
#         if screenshot_done:
#             status_text = "INTRUDER LOGGED"
#             color = (255, 0, 0) 
#         else:
#             status_text = f"UNKNOWN USER! Alert in: {max(0, 3 - int(time_elapsed))}s"
#             color = (0, 0, 255) 

#             if time_elapsed > 3:
#                 save_intruder_screenshot(frame)
#                 screenshot_done = True
#     else:
#         # CAMERA KHALI HAI
#         eye_label, eye_color = get_eye_status(frame) 
#         status_text = f"NO FACE - {eye_label}"
#         color = (255, 255, 255)
#         unknown_timer_start = None

#     # --- STEP 5: VISUALS ---
#     for (top, right, bottom, left) in face_locations:
#         top *= 4; right *= 4; bottom *= 4; left *= 4
#         cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

#     # Screen UI
#     cv2.putText(frame, status_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
#     cv2.imshow("Akhil's Smart Monitor", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()




### Updated `main.py` (High Accuracy Version)

# import threading
# from modules.remote_handler import listen_for_commands

# import cv2
# import face_recognition
# import time
# import os
# import numpy as np
# # Humare modules import kar rahe hain
# from modules.security_actions import save_intruder_screenshot
# from modules.eye_tracking import get_eye_status 

# # --- STEP 1: SMART SETUP ---
# known_face_encodings = []
# known_face_names = []
# faces_folder = "data/known_faces/"

# print("⌛ Loading all face angles for better accuracy...")

# if not os.path.exists(faces_folder):
#     os.makedirs(faces_folder)

# for file_name in os.listdir(faces_folder):
#     if file_name.endswith((".jpg", ".png", ".jpeg")):
#         img_path = os.path.join(faces_folder, file_name)
#         image = face_recognition.load_image_file(img_path)
#         encoding = face_recognition.face_encodings(image)
        
#         if len(encoding) > 0:
#             known_face_encodings.append(encoding[0])
#             known_face_names.append("Akhil")
#             print(f"✅ Loaded: {file_name}")

# if not known_face_encodings:
#     print("❌ ERROR: Photos nahi mili! Pehle trainer.py chalayein.")
#     exit()

# # --- STEP 2: INITIALIZE ---
# cap = cv2.VideoCapture(0)
# unknown_timer_start = None
# screenshot_done = False 

# print("🛡️ Guard Active: Scanning for Akhil...")

# while True:
#     ret, frame = cap.read()
#     if not ret: break
    
#     # Natural View ke liye flip
#     frame = cv2.flip(frame, 1) 

#     # Processing speed ke liye resize
#     small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#     rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

#     face_locations = face_recognition.face_locations(rgb_small_frame)
#     face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#     is_akhil_present = False
    
#     # --- STEP 3: ALL PHOTO COMPARISON (DISTANCE LOGIC) ---
#     for encoding in face_encodings:
#         # Saari photos se distance calculate karein
#         face_distances = face_recognition.face_distance(known_face_encodings, encoding)
        
#         if len(face_distances) > 0:
#             best_match_index = np.argmin(face_distances) # Sabse kareebi photo dhundhein
            
#             # Agar distance 0.50 se kam hai, toh matlab wo Akhil hai
#             # (Chhota number = Jyada match)
#             if face_distances[best_match_index] <= 0.50:
#                 is_akhil_present = True
#                 break

#     # --- STEP 4: EYE TRACKING & LOGIC ---
#     if is_akhil_present:
#         eye_label, eye_color = get_eye_status(frame)
        
#         if "LOOKING" in eye_label and "NOT" not in eye_label:
#             status_text = "AKHIL PRESENT - SAFE"
#             color = (0, 255, 0)
#         else:
#             status_text = f"ATTENTION: {eye_label}"
#             color = eye_color
            
#         unknown_timer_start = None
#         screenshot_done = False 
    
#     elif len(face_encodings) > 0:
#         if unknown_timer_start is None:
#             unknown_timer_start = time.time()
        
#         time_elapsed = time.time() - unknown_timer_start
        
#         if screenshot_done:
#             status_text = "INTRUDER LOGGED"
#             color = (255, 0, 0) 
#         else:
#             status_text = f"UNKNOWN! Alert in: {max(0, 3 - int(time_elapsed))}s"
#             color = (0, 0, 255) 

#             if time_elapsed > 3:
#                 save_intruder_screenshot(frame)
#                 screenshot_done = True
#     else:
#         eye_label, eye_color = get_eye_status(frame) 
#         status_text = f"NO FACE - {eye_label}"
#         color = (255, 255, 255)
#         unknown_timer_start = None

#     # --- STEP 5: VISUALS ---
#     for (top, right, bottom, left) in face_locations:
#         top *= 4; right *= 4; bottom *= 4; left *= 4
#         cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

#     cv2.putText(frame, status_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
#     cv2.imshow("AI Monitor", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()





### Updated `main.py` (Isse replace karein):*********************************


import sys, os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
resource_path("face_recognition_models/models/shape_predictor_68_face_landmarks.dat")

import threading
from modules.remote_handler import listen_for_commands # Aapka naya module

import cv2
import face_recognition
import time
import os
import numpy as np
# Humare modules import kar rahe hain
from modules.security_actions import save_intruder_screenshot
from modules.eye_tracking import get_eye_status 
from modules.wallpaper_manager import show_friendly, show_alert, show_idle

# --- STEP 1: SMART SETUP ---
known_face_encodings = []
known_face_names = []
faces_folder = "data/known_faces/"

# 🔥 BADLAV: Telegram Listener ko alag "Thread" mein chalu karna
print("📡 Starting Telegram Remote Listener...")
telegram_thread = threading.Thread(target=listen_for_commands, daemon=True)
telegram_thread.start()

print("⌛ Loading all face angles for better accuracy...")

if not os.path.exists(faces_folder):
    os.makedirs(faces_folder)

for file_name in os.listdir(faces_folder):
    if file_name.endswith((".jpg", ".png", ".jpeg")):
        img_path = os.path.join(faces_folder, file_name)
        image = face_recognition.load_image_file(img_path)
        encoding = face_recognition.face_encodings(image)
        
        if len(encoding) > 0:
            known_face_encodings.append(encoding[0])
            known_face_names.append("Akhil")
            print(f"✅ Loaded: {file_name}")

if not known_face_encodings:
    print("❌ ERROR: Photos nahi mili! Pehle trainer.py chalayein.")
    exit()

# --- STEP 2: INITIALIZE ---
cap = cv2.VideoCapture(0)
unknown_timer_start = None
screenshot_done = False 

print("🛡️ Guard Active: Scanning for Akhil...")

while True:
    ret, frame = cap.read()
    if not ret: break
    
    # Natural View ke liye flip
    frame = cv2.flip(frame, 1) 

    # Processing speed ke liye resize
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    is_akhil_present = False
    
    # --- STEP 3: ALL PHOTO COMPARISON ---
    for encoding in face_encodings:
        face_distances = face_recognition.face_distance(known_face_encodings, encoding)
        
        if len(face_distances) > 0:
            best_match_index = np.argmin(face_distances) 
            if face_distances[best_match_index] <= 0.40:
                is_akhil_present = True
                break

    # --- STEP 4: EYE TRACKING & LOGIC ---
    if is_akhil_present:
        eye_label, eye_color = get_eye_status(frame)
        
        if "LOOKING" in eye_label and "NOT" not in eye_label:
            status_text = "AKHIL PRESENT - SAFE"
            color = (0, 255, 0)
        else:
            status_text = f"ATTENTION: {eye_label}"
            color = eye_color
            
        unknown_timer_start = None
        screenshot_done = False 
    
    elif len(face_encodings) > 0:
        if unknown_timer_start is None:
            unknown_timer_start = time.time()
        
        time_elapsed = time.time() - unknown_timer_start
        
        if screenshot_done:
            status_text = "INTRUDER LOGGED - CHECK TELEGRAM"
            color = (255, 0, 0) 
        else:
            status_text = f"UNKNOWN! Alert in: {max(0, 3 - int(time_elapsed))}s"
            color = (0, 0, 255) 

            if time_elapsed > 3:
                save_intruder_screenshot(frame)
                screenshot_done = True
    else:
        eye_label, eye_color = get_eye_status(frame) 
        status_text = f"NO FACE - {eye_label}"
        color = (255, 255, 255)
        unknown_timer_start = None

    # --- STEP 5: VISUALS ---
    for (top, right, bottom, left) in face_locations:
        top *= 4; right *= 4; bottom *= 4; left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

    cv2.putText(frame, status_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
    cv2.imshow("AI Monitor", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


from modules.ai_voice import generate_ai_voice
from modules.llm_report import generate_report
from modules.security_actions import send_gmail_report

event = "Unknown person detected near your laptop."

report = generate_report(event)
audio = generate_ai_voice(report)

send_gmail_report(report, audio)

# *************************************



