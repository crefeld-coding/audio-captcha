"""Audio-Captcha Main"""

import pocketsphinx
import pyttsx3 as tts
import random
import speech_recognition as sr

# Global Vars
r = sr.Recognizer()
mic = sr.Microphone()
engine = tts.init()

PASSWORDS = ("swordfish", "alpha", "bravo", "charlie", "delta", "echo", "foxtrot")


def voice_input(passphrase):

    global mic
    global r
    global engine

    engine.say("Please repeat the following pass phrase")
    engine.say(" ".join(passphrase))
    engine.runAndWait()

    with mic as source:
        try:
            audio = r.listen(source)
            engine.say("Please wait")
            engine.runAndWait()
            transcription = r.recognize_google(audio)
            print(f"Input was: {transcription}")

            return transcription.lower()

        except sr.UnknownValueError:
            print("unrecognizable input")
            return "unrecognizable input"


def construct_passphrase():
    """Creates a passphrase of 3 words from the global tuple PASSWORDS, returns a string"""
    global PASSWORDS
    passphrase = list()
    for i in range(3):
        passphrase.append(PASSWORDS[random.randint(0, len(PASSWORDS) - 1)])
    return passphrase


def verify_human():
    passphrase = construct_passphrase()
    passphrase_entered = voice_input(passphrase)
    if passphrase_entered == " ".join(passphrase):
        print("Test Cleared")
    else:
        print("Test Failed")


if __name__ == "__main__":
    verify_human()
