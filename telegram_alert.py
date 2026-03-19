import requests
from modules.llm_report import generate_report   # import report generator

TELEGRAM_TOKEN = "8297500439:AAEwyZqGH77OsdHbp46y6IrC1RQpcaP8DKo"
TELEGRAM_CHAT_ID = "8465690128"

def send_telegram(msg: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": msg}
    requests.post(url, data=data)


# create event text
event = "Unknown person detected at laptop"

# generate intelligent report
report = generate_report(event)

# now send it
send_telegram(report)