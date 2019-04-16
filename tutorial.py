"""RealPython SpeechRecognition Tutorial"""

import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

# Microphone stuff
with mic as source:

    try:
        audio = r.listen(source)
        print(r.recognize_google(audio))

    except sr.UnknownValueError:
        print("Failed Input")


# Tutorial: https://realpython.com/python-speech-recognition/
