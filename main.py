"""Audio-Captcha Main"""

import gtts
from io import BytesIO
import pocketsphinx
from pydub import AudioSegment
from pydub.playback import play
import pyttsx3
import random
import speech_recognition as sr

# Global Vars
r = sr.Recognizer()
mic = sr.Microphone()
engine = pyttsx3.init()

DEBUGGING = True
PASSWORDS = ("swordfish", "alpha", "bravo", "charlie", "delta", "echo", "foxtrot")


def debug_print(text):
    if DEBUGGING:
        print(text)


def voice_output(string):
    debug_print("starting tts")
    mp3_fp = BytesIO()
    tts = gtts.gTTS(string, 'en')
    tts.write_to_fp(mp3_fp)
    audio = AudioSegment.from_mp3(mp3_fp)
    play(audio)
    debug_print("tts end")


def voice_input(passphrase):

    global mic
    global r
    global engine

    voice_output("Please repeat the following pass phrase")
    voice_output(" ".join(passphrase))

    with mic as source:
        try:
            debug_print("recording")
            audio = r.listen(source)
            debug_print("recorded")
            voice_output("Please wait")
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
