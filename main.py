"""Audio-Captcha Main"""

import speech_recognition as sr
import pyttsx3 as tts

# Global Vars
r = sr.Recognizer()
mic = sr.Microphone()
engine = tts.init()


def voice_input(prompt):

    engine.say("Please repeat the following pass phrase")
    engine.say(prompt)
    engine.runAndWait()

    with mic as source:
        try:
            audio = r.listen(source)
            engine.say("Please wait")
            engine.runAndWait()
            return r.recognize_google(audio)

        except sr.UnknownValueError:
            pass


print(voice_input("swordfish"))
