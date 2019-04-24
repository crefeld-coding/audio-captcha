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

    os.system("say please repeat the following pass phrase")
    os.system(f"say {passphrase}")

    with mic as source:
        try:
            audio = r.listen(source)
            transcription = r.recognize_google(audio)
            os.system("say please wait")
            return transcription.lower()

        except sr.UnknownValueError:
            return 1


def construct_passphrase():
    """Creates a passphrase of 3 words from the global tuple PASSPHRASES, returns a string"""
    global PASSPHRASES
    passphrase = list()
    for i in range(3):
        passphrase.append(PASSPHRASES[random.randint(0, len(PASSPHRASES)-1)])
    passphrase = " ".join(passphrase)
    return passphrase.lower()


def verify_human():
    passphrase = construct_passphrase()
    passphrase_entered = voice_input(passphrase)
    if passphrase_entered == passphrase:
        return 0
    elif passphrase_entered == 1:
        os.system("say unrecognisable input, please try again")
        return 1
    else:
        os.system("say test failed")
        return 2


if __name__ == "__main__":
    failed_tests = 0
    while True:
        last_test = verify_human()
        if last_test == 0:
            os.system("say test cleared")
            break
        else:
            failed_tests += 1
        if failed_tests >= 3:
            os.system("say access denied")
            break
        os.system("say please try again")
