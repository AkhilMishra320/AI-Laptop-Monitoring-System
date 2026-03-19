
# ### 1. `modules/remote_handler.py` ka code:


# import requests
# import os
# import time

# # --- CONFIGURATION ---
# # Wahi Token daalein jo aapne pehle use kiya tha
# TELEGRAM_TOKEN = "8297500439:AAEwyZqGH77OsdHbp46y6IrC1RQpcaP8DKo"

# def listen_for_commands():
#     last_update_id = 0
#     print("📡 Remote Handler: Telegram signals check kar raha hoon...")
    
#     while True:
#         try:
#             # Telegram API se naye signals (updates) maangna
#             url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates?offset={last_update_id + 1}&timeout=30"
#             response = requests.get(url).json()
            
#             if response["result"]:
#                 for update in response["result"]:
#                     last_update_id = update["update_id"]
                    
#                     # Agar user ne button dabaya hai
#                     if "callback_query" in update:
#                         command = update["callback_query"]["data"]
#                         user_id = update["callback_query"]["from"]["id"]
#                         query_id = update["callback_query"]["id"]
                        
#                         # 1. Agar SLEEP dabaya
#                         if command == "sleep":
#                             print("🚨 Remote Command: SLEEP detected!")
#                             # User ko confirmation bhejna
#                             requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={user_id}&text=Command Received: Sleeping Now... 😴")
                            
#                             # Windows Sleep Command
#                             # Ye command computer ko sleep mode mein daal deti hai
#                             os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                            
#                         # 2. Agar ALLOW dabaya
#                         elif command == "allow":
#                             print("✅ Remote Command: ALLOW detected!")
#                             requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={user_id}&text=Access Granted! Laptop normal chalta rahega.")

#                         # Telegram ko notification bhejna ki action le liya gaya hai (Loading hatane ke liye)
#                         requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/answerCallbackQuery?callback_query_id={query_id}")

#         except Exception as e:
#             # Kabhi network error aaye toh script crash na ho
#             print(f"⚠️ Connection Error in Remote Handler: {e}")
#             time.sleep(5)
#             continue
        
#         # CPU par load kam karne ke liye chota pause
#         time.sleep(1)



### Updated `modules/remote_handler.py` (Isse replace karein):

import requests
import os
import time

# --- CONFIGURATION ---
TELEGRAM_TOKEN = "8297500439:AAEwyZqGH77OsdHbp46y6IrC1RQpcaP8DKo"
BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

def listen_for_commands():
    # 🔥 STEP 1: Pehle purane saare faltu messages ko skip karo
    print("🧹 Cleaning old Telegram messages...")
    last_update_id = 0
    
    # Ek baar check karke sabse latest ID le lete hain
    try:
        response = requests.get(f"{BASE_URL}/getUpdates").json()
        if response.get("result"):
            last_update_id = response["result"][-1]["update_id"]
            print(f"✅ Old messages skipped up to ID: {last_update_id}")
    except Exception as e:
        print(f"⚠️ Initial cleanup error: {e}")

    print("📡 Remote Handler: Ready for NEW commands only!")
    
    while True:
        try:
            # offset={last_update_id + 1} ka matlab hai ki purane wale dobara mat dikhao
            url = f"{BASE_URL}/getUpdates?offset={last_update_id + 1}&timeout=30"
            response = requests.get(url).json()
            
            if response.get("result"):
                for update in response["result"]:
                    last_update_id = update["update_id"]
                    
                    if "callback_query" in update:
                        command = update["callback_query"]["data"]
                        user_id = update["callback_query"]["from"]["id"]
                        query_id = update["callback_query"]["id"]
                        
                        # Loading icon hatane ke liye turant answer karein
                        requests.post(f"{BASE_URL}/answerCallbackQuery?callback_query_id={query_id}")

                        if command == "sleep":
                            print("🚨 Command: SLEEP")
                            requests.get(f"{BASE_URL}/sendMessage?chat_id={user_id}&text=Command Received: Sleeping Now... 😴")
                            # 1 second wait taaki message chala jaye
                            time.sleep(1)
                            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                            
                        elif command == "allow":
                            print("✅ Command: ALLOW")
                            # Ek baar hi message bheje
                            requests.get(f"{BASE_URL}/sendMessage?chat_id={user_id}&text=Access Granted! ✅")

        except Exception as e:
            print(f"⚠️ Connection Error: {e}")
            time.sleep(2)






