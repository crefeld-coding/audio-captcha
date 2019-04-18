"""Audio-Captcha Main"""

import gtts
import pocketsphinx
import pyttsx3 as tts
from pydub import AudioSegment
from pydub.playback import play
import random
import speech_recognition as sr

# Global Vars
r = sr.Recognizer()
mic = sr.Microphone()
engine = tts.init()

DEBUGGING = True
PASSWORDS = ("swordfish", "alpha", "bravo", "charlie", "delta", "echo", "foxtrot")


def debug_print(text):
    if DEBUGGING:
        print(text)


def voice_input(passphrase):

    global mic
    global r
    global engine

    engine.say("Please repeat the following pass phrase")
    engine.say(" ".join(passphrase))
    debug_print("starting tts")
    engine.runAndWait()
    debug_print("tts end")

    with mic as source:
        try:
            debug_print("recording")
            audio = r.listen(source)
            debug_print("recorded")
            engine.say("Please wait")
            debug_print("starting tts")
            engine.runAndWait()
            debug_print("tts end")
            debug_print("starting transcription")
            transcription = r.recognize_google(audio)
            debug_print("transcription end")
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
