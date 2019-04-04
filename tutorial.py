"""RealPython SpeechRecognition Tutorial"""

import speech_recognition as sr

r = sr.Recognizer()

harvard = sr.AudioFile('harvard.wav')
jackhammer = sr.AudioFile('jackhammer.wav')
with harvard as source:
    audio1 = r.record(source, duration=4)
with jackhammer as source:
    r.adjust_for_ambient_noise(source, duration=.5)
    audio2 = r.record(source, duration=4)

print(r.recognize_google(audio1) + '  !=  ' + r.recognize_google(audio2))
