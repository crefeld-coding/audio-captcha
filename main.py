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
            print(f"Input was: {transcription.lower()}")
            os.system("say please wait")
            return transcription.lower()

        except sr.UnknownValueError:
            print("unrecognizable input")
            return "unrecognizable input"


def construct_passphrase():
    """Creates a passphrase of 3 words from the global tuple PASSPHRASES, returns a string"""
    global PASSPHRASES
    passphrase = list()
    for i in range(3):
        passphrase.append(PASSPHRASES[random.randint(0, len(PASSPHRASES)-1)])
    passphrase = " ".join(passphrase)
    print(f'Passphrase was:  {passphrase}')
    return passphrase.lower()


def verify_human():
    passphrase = construct_passphrase()
    passphrase_entered = voice_input(passphrase)
    if passphrase_entered == passphrase:
        print("Test Cleared")
    else:
        print("Test Failed")


if __name__ == "__main__":
    verify_human()
