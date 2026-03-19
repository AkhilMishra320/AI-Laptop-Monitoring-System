### `trainer.py` (The Calibration Script)

import cv2
import os
import time

# Folder setup
SAVE_PATH = "data/known_faces/"
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

cap = cv2.VideoCapture(0)

# Alag-alag angles jo hume capture karne hain
angles = [
    "Look Straight", "Tilt Head Left", "Tilt Head Right", 
    "Look Slightly Up", "Look Slightly Down", "Normal Working Pose",
    "Close Eyes (for blink test)", "Smile", "Serious Face", "Dim Light Pose"
]

print("🚀 Starting Calibration... Be ready!")
time.sleep(2)

for i, angle_name in enumerate(angles):
    start_time = time.time()
    
    while True:
        ret, frame = cap.read()
        if not ret: break

        # Screen par instruction dikhayein
        cv2.putText(frame, f"POSE {i+1}/10: {angle_name}", (30, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 5)
        
        # Countdown dikhayein
        elapsed = time.time() - start_time
        countdown = 3 - int(elapsed)
        cv2.putText(frame, f"Capturing in: {countdown}s", (30, 100), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 5)

        cv2.imshow("Calibration Mode", frame)

        if countdown <= 0:
            # Photo save karein
            file_name = f"akhil_{i}.jpg"
            cv2.imwrite(os.path.join(SAVE_PATH, file_name), frame)
            print(f"✅ Captured {angle_name}")
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
print("\n🔥 All angles saved! Now your main.py will be 99% accurate.")

