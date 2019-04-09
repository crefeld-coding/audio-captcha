"""RealPython SpeechRecognition Tutorial"""

import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

# Speech Recognition Stuff:
# harvard = sr.AudioFile('harvard.wav')
# jackhammer = sr.AudioFile('jackhammer.wav')
# with harvard as source:
#     audio1 = r.record(source, duration=4)
# with jackhammer as source:
#     r.adjust_for_ambient_noise(source, duration=.5)
#     audio2 = r.record(source, duration=4)

# Microphone stuff
with mic as source:

    try:
        audio = r.listen(source)
        print(r.recognize_google(audio))

    except sr.UnknownValueError:
        print("Failed Input")


# Tutorial: https://realpython.com/python-speech-recognition/
