

# ### 1️⃣ File: `modules/security_actions.py`

# import cv2
# import datetime
# import os

# def save_intruder_screenshot(frame):
#     # Folder check karo, agar nahi hai toh banao
#     folder = "data/screenshots"
#     if not os.path.exists(folder):
#         os.makedirs(folder, exist_ok=True)

#     # Time ke saath unique filename
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     file_path = os.path.join(folder, f"intruder_{timestamp}.jpg")
    
#     # Image save karo
#     cv2.imwrite(file_path, frame)
#     print(f"⚠️ ALERT: Screenshot saved at {file_path}")
#     return file_path



### Updated `modules/security_actions.py`


# import cv2
# import os
# import smtplib
# from email.message import EmailMessage
# import datetime

# # --- SETTINGS ---
# SENDER_EMAIL = "akhilmishra99420@gmail.com"  # Aapki email
# SENDER_PASSWORD = "awov vewu antg hlye" # 16-digit App Password
# RECEIVER_EMAIL = "akhilmishra99420@gmail.com" # Jahan photo chahiye

# def send_email_alert(image_path):
#     msg = EmailMessage()
#     msg['Subject'] = "🚨 INTRUDER ALERT: Unauthorized Access Detected!"
#     msg['From'] = SENDER_EMAIL
#     msg['To'] = RECEIVER_EMAIL
#     msg.set_content(f"Warning! An unknown person was detected on your laptop at {datetime.datetime.now()}. Check the attached screenshot.")

#     # Photo attach karein
#     with open(image_path, 'rb') as f:
#         file_data = f.read()
#         file_name = os.path.basename(image_path)
#         msg.add_attachment(file_data, maintype='image', subtype='jpg', filename=file_name)

#     try:
#         with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#             smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
#             smtp.send_message(msg)
#             print("📧 Email alert sent successfully!")
#     except Exception as e:
#         print(f"❌ Failed to send email: {e}")

# def save_intruder_screenshot(frame):
#     if not os.path.exists("intruders"):
#         os.makedirs("intruders")
    
#     timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#     file_path = f"intruders/intruder_{timestamp}.jpg"
#     cv2.imwrite(file_path, frame)
#     print(f"📸 Screenshot saved: {file_path}")
    
#     # Screenshot save hote hi email bhej dein
#     send_email_alert(file_path)


# ### Important: Google "App Password" Kaise Banayein?






### Step 1: Telegram Bot Token aur Chat ID lein



### Step 2: `modules/security_actions.py` ko Update karein

# import cv2
# import os
# import smtplib
# import requests
# import datetime
# from email.message import EmailMessage

# # --- CONFIGURATION ---
# SENDER_EMAIL = "akhilmishra99420@gmail.com"
# SENDER_PASSWORD = "awov vewu antg hlye"  # Wo 16-digit code
# RECEIVER_EMAIL = "akhilmishra99420@gmail.com"

# TELEGRAM_TOKEN = "8297500439:AAEwyZqGH77OsdHbp46y6IrC1RQpcaP8DKo"
# TELEGRAM_CHAT_ID = "8465690128"

# def send_gmail(image_path):
#     msg = EmailMessage()
#     msg['Subject'] = "🚨 GMAIL ALERT: Intruder Detected!"
#     msg['From'] = SENDER_EMAIL
#     msg['To'] = RECEIVER_EMAIL
#     msg.set_content(f"Intruder detected at {datetime.datetime.now()}. Control via Telegram.")

#     with open(image_path, 'rb') as f:
#         msg.add_attachment(f.read(), maintype='image', subtype='jpg', filename="intruder.jpg")

#     try:
#         with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#             smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
#             smtp.send_message(msg)
#             print("📧 Gmail sent.")
#     except: print("❌ Gmail failed.")

# def send_telegram(image_path):
#     # Photo bhejte hain saath mein Yes/No buttons ke
#     url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
    
#     # Ye buttons banate hain
#     buttons = {
#         "inline_keyboard": [[
#             {"text": "✅ ALLOW", "callback_data": "allow"},
#             {"text": "❌ SLEEP", "callback_data": "sleep"}
#         ]]
#     }
    
#     files = {'photo': open(image_path, 'rb')}
#     data = {
#         'chat_id': TELEGRAM_CHAT_ID,
#         'caption': "🚨 INTRUDER DETECTED! Kya karna hai?",
#         'reply_markup': str(buttons).replace("'", '"')
#     }
    
#     try:
#         requests.post(url, files=files, data=data)
#         print("📲 Telegram alert sent with buttons.")
#     except: print("❌ Telegram failed.")

# def save_intruder_screenshot(frame):
#     if not os.path.exists("intruders"): os.makedirs("intruders")
#     timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#     file_path = f"intruders/intruder_{timestamp}.jpg"
#     cv2.imwrite(file_path, frame)
    
#     # Dono jagah alert bhejte hain
#     send_gmail(file_path)
#     send_telegram(file_path)



# ### Agla Step: Buttons ko "Asli" banana




# import cv2
# import os
# import smtplib
# import requests
# import datetime
# import json # JSON handle karne ke liye
# from email.message import EmailMessage

# # --- CONFIGURATION ---
# SENDER_EMAIL = "akhilmishra99420@gmail.com"
# SENDER_PASSWORD = "awov vewu antg hlye"
# RECEIVER_EMAIL = "akhilmishra99420@gmail.com"

# TELEGRAM_TOKEN = "8297500439:AAEwyZqGH77OsdHbp46y6IrC1RQpcaP8DKo"
# TELEGRAM_CHAT_ID = "8465690128"

# def send_gmail(image_path):
#     msg = EmailMessage()
#     msg['Subject'] = "🚨 GMAIL ALERT: Intruder Detected!"
#     msg['From'] = SENDER_EMAIL
#     msg['To'] = RECEIVER_EMAIL
#     msg.set_content(f"Intruder detected at {datetime.datetime.now()}. Control via Telegram.")

#     with open(image_path, 'rb') as f:
#         msg.add_attachment(f.read(), maintype='image', subtype='jpg', filename="intruder.jpg")

#     try:
#         with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#             smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
#             smtp.send_message(msg)
#             print("📧 Gmail sent.")
#     except: print("❌ Gmail failed.")


# # #    *****************************************************

# def send_gmail_report(report_text, audio_file=None):
#     msg = EmailMessage()
#     msg['Subject'] = "🧠 AI Security Report"
#     msg['From'] = SENDER_EMAIL
#     msg['To'] = RECEIVER_EMAIL
#     msg.set_content(report_text)

#     if audio_file:
#         with open(audio_file, 'rb') as f:
#             msg.add_attachment(
#                 f.read(),
#                 maintype='audio',
#                 subtype='mpeg',
#                 filename="AI_voice_alert.mp3"
#             )

#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#         smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
#         smtp.send_message(msg)



# def send_telegram(image_path):
#     url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
    
#     # Starting buttons: Sirf Allow aur Sleep
#     buttons = {
#         "inline_keyboard": [[
#             {"text": "✅ ALLOW", "callback_data": "ask_time"}, # "allow" ko "ask_time" kar diya
#             {"text": "❌ SLEEP", "callback_data": "sleep"}
#         ]]
#     }
    
#     files = {'photo': open(image_path, 'rb')}
#     data = {
#         'chat_id': TELEGRAM_CHAT_ID,
#         'caption': "🚨 INTRUDER DETECTED! Kya karna hai?",
#         'reply_markup': json.dumps(buttons) # Clean JSON format
#     }
    
#     try:
#         requests.post(url, files=files, data=data)
#         print("📲 Telegram alert sent.")
#     except Exception as e: 
#         print(f"❌ Telegram failed: {e}")

# # Naya Function: Time options dikhane ke liye
# def send_time_options(chat_id, message_id):
#     url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/editMessageCaption"
    
#     time_buttons = {
#         "inline_keyboard": [
#             [
#                 {"text": "5m", "callback_data": "allow_5"},
#                 {"text": "10m", "callback_data": "allow_10"},
#                 {"text": "20m", "callback_data": "allow_20"}
#             ],
#             [
#                 {"text": "60m", "callback_data": "allow_60"},
#                 {"text": "Always", "callback_data": "allow_always"}
#             ]
#         ]
#     }
    
#     data = {
#         'chat_id': chat_id,
#         'message_id': message_id,
#         'caption': "Kitni der ke liye allow karna hai?",
#         'reply_markup': json.dumps(time_buttons)
#     }
#     requests.post(url, data=data)

# def save_intruder_screenshot(frame):
#     if not os.path.exists("intruders"): os.makedirs("intruders")
#     timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#     file_path = f"intruders/intruder_{timestamp}.jpg"
#     cv2.imwrite(file_path, frame)
    
#     send_gmail(file_path)
#     send_telegram(file_path)



# # from modules.wallpaper_manager import show_friendly, show_alert, show_idle

# # ### Kya badlav kiya maine?


# # from modules.llm_report import generate_report

# # event = "Unknown person detected at 14:32"
# # report = generate_report(event)

# # send_gmail(report)





import cv2
import os
import smtplib
import requests
import datetime
import json
from email.message import EmailMessage

# --- CONFIGURATION ---
SENDER_EMAIL = "akhilmishra99420@gmail.com"
SENDER_PASSWORD = "awov vewu antg hlye"
RECEIVER_EMAIL = "akhilmishra99420@gmail.com"

TELEGRAM_TOKEN = "8297500439:AAEwyZqGH77OsdHbp46y6IrC1RQpcaP8DKo"
TELEGRAM_CHAT_ID = "8465690128"


# ------------------ NORMAL GMAIL ALERT (IMAGE) ------------------
def send_gmail(image_path):
    msg = EmailMessage()
    msg['Subject'] = "🚨 GMAIL ALERT: Intruder Detected!"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg.set_content(f"Intruder detected at {datetime.datetime.now()}.")

    with open(image_path, 'rb') as f:
        msg.add_attachment(
            f.read(),
            maintype='image',
            subtype='jpeg',
            filename="intruder.jpg"
        )

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
            print("📧 Screenshot email sent")
    except Exception as e:
        print("❌ Gmail failed:", e)


# ------------------ AI REPORT GMAIL WITH VOICE ------------------
# def send_gmail_report(report_text, audio_file=None):
#     msg = EmailMessage()
#     msg['Subject'] = "🧠 AI Security Report"
#     msg['From'] = SENDER_EMAIL
#     msg['To'] = RECEIVER_EMAIL
#     msg.set_content(report_text)

#     try:
#         # attach voice file if exists
#         if audio_file and os.path.exists(audio_file):
#             print("🎤 Attaching AI voice:", audio_file)
#             with open(audio_file, 'rb') as f:
#                 msg.add_attachment(
#                     f.read(),
#                     maintype='audio',
#                     subtype='mpeg',
#                     filename=os.path.basename(audio_file)
#                 )
#         else:
#             print("⚠ Voice file not found:", audio_file)

#         # send mail
#         with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#             smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
#             smtp.send_message(msg)

#         print("📧 AI report email sent with voice")

#     except Exception as e:
#         print("❌ Gmail report failed:", e)


def send_gmail_report(report_text, audio_file=None):
    import mimetypes

    msg = EmailMessage()
    msg['Subject'] = "🧠 AI Security Report"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg.set_content(report_text)

    try:
        # attach audio safely
        if audio_file and os.path.exists(audio_file):
            print("🎤 Attaching:", audio_file)

            ctype, encoding = mimetypes.guess_type(audio_file)
            if ctype is None or encoding is not None:
                ctype = 'application/octet-stream'

            maintype, subtype = ctype.split('/', 1)

            with open(audio_file, 'rb') as f:
                msg.add_attachment(
                    f.read(),
                    maintype=maintype,
                    subtype=subtype,
                    filename=os.path.basename(audio_file)
                )
        else:
            print("⚠ Audio file missing:", audio_file)

        # send mail
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)

        print("📧 Email sent WITH voice attachment")

    except Exception as e:
        print("❌ Gmail voice send error:", e)


# ------------------ TELEGRAM ALERT ------------------
def send_telegram(image_path):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"

    buttons = {
        "inline_keyboard": [[
            {"text": "✅ ALLOW", "callback_data": "ask_time"},
            {"text": "❌ SLEEP", "callback_data": "sleep"}
        ]]
    }

    files = {'photo': open(image_path, 'rb')}
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'caption': "🚨 INTRUDER DETECTED! Kya karna hai?",
        'reply_markup': json.dumps(buttons)
    }

    try:
        requests.post(url, files=files, data=data)
        print("📲 Telegram alert sent")
    except Exception as e:
        print("❌ Telegram failed:", e)


# ------------------ TELEGRAM TIME OPTIONS ------------------
def send_time_options(chat_id, message_id):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/editMessageCaption"

    time_buttons = {
        "inline_keyboard": [
            [
                {"text": "5m", "callback_data": "allow_5"},
                {"text": "10m", "callback_data": "allow_10"},
                {"text": "20m", "callback_data": "allow_20"}
            ],
            [
                {"text": "60m", "callback_data": "allow_60"},
                {"text": "Always", "callback_data": "allow_always"}
            ]
        ]
    }

    data = {
        'chat_id': chat_id,
        'message_id': message_id,
        'caption': "Kitni der ke liye allow karna hai?",
        'reply_markup': json.dumps(time_buttons)
    }

    requests.post(url, data=data)


# ------------------ SAVE SCREENSHOT + ALERT ------------------
# def save_intruder_screenshot(frame):
#     if not os.path.exists("intruders"):
#         os.makedirs("intruders")

#     timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#     file_path = f"intruders/intruder_{timestamp}.jpg"
#     cv2.imwrite(file_path, frame)

#     send_gmail(file_path)
#     send_telegram(file_path)


def save_intruder_screenshot(frame):
    if not os.path.exists("intruders"):
        os.makedirs("intruders")

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"intruders/intruder_{timestamp}.jpg"
    cv2.imwrite(file_path, frame)

    # --- NORMAL ALERTS ---
    send_gmail(file_path)
    send_telegram(file_path)

    # --- AI REPORT + VOICE ---
    try:
        from modules.llm_report import generate_report
        from modules.ai_voice import generate_ai_voice
        from modules.security_actions import send_gmail_report

        event = f"Unknown person detected at {timestamp}"
        report = generate_report(event)
        audio = generate_ai_voice(report)

        send_gmail_report(report, audio)

        print("🧠 AI report + voice sent")

    except Exception as e:
        print("❌ AI report failed:", e)


# from twilio.rest import Client

# ACCOUNT_SID = "your_sid"
# AUTH_TOKEN = "your_token"

# client = Client(ACCOUNT_SID, AUTH_TOKEN)

# def send_sms(message):
#     client.messages.create(
#         body=message,
#         from_="+1xxxxxxxxxx",   # Twilio number
#         to="+919942087716"      # your phone number
#     )

# send_sms("⚠ Unknown person detected near your laptop")