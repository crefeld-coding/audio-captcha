"""Audio-Captcha Main"""

import speech_recognition as sr
import pyttsx3 as tts
import random
import os

# Global Vars
r = sr.Recognizer()
mic = sr.Microphone()
engine = tts.init()
PASSPHRASES = ("swordfish", "alpha", "bravo", "charlie", "delta", "echo", "foxtrot")


def voice_input(passphrase):

    os.system("say Please repeat the following pass phrase")
    os.system(f"say {passphrase}")

    with mic as source:
        try:
            audio = r.listen(source)
            transcription = r.recognize_google(audio)
            print(f"Input was: {transcription}")
            return transcription
            os.system("say please wait")

        except sr.UnknownValueError:
            print("unrecognizable input")
            return "unrecognizable input"


def construct_passphrase():
    """Creates a passphrase of 3 words from the global tuple PASSPHRASES, returns a string"""
    global PASSPHRASES
    passphrase = str()
    for i in range(3):
        passphrase += (PASSPHRASES[random.randint(0, len(PASSPHRASES)-1)] + " ")
    return passphrase


def verify_human():
    passphrase = construct_passphrase().lower()
    passphrase_entered = voice_input(passphrase).lower()
    if passphrase_entered == passphrase:
        print("Test Cleared")
    else:
        print("Test Failed")


if __name__ == "__main__":
    verify_human()
