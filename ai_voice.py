def generate_ai_voice(text, filename="ai_alert.mp3"):
    from gtts import gTTS
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    print("VOICE SAVED AT:", filename)
    return filename