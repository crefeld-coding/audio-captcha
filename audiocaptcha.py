"""Audio-Captcha Main"""

from exitstatus import ExitStatus
import speech_recognition as sr
import random
import os
import sys

# Global Vars
r = sr.Recognizer()
mic = sr.Microphone()
PASSPHRASES = ("swordfish", "alpha", "bravo", "charlie", "delta", "echo", "foxtrot")


def get_user_attempt(passphrase):

    os.system("say please repeat the following pass phrase")
    os.system(f"say {passphrase}")

    with mic as source:
        try:
            audio = r.listen(source)
            transcription = r.recognize_google(audio)
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


def run_test():
    passphrase = construct_passphrase()
    passphrase_entered = get_user_attempt(passphrase)
    if passphrase_entered == passphrase:
        return 0
    elif passphrase_entered == 1:
        os.system("say unrecognisable input")
        return 1
    else:
        os.system("say test failed")
        return 2


def verify_human():
    failed_tests = 0
    bad_inputs = 0
    while True:
        last_test = run_test()

        # tests and keeps track of what verify_human() returned, returns success if test passed
        if last_test == 0:
            os.system("say test cleared")
            return ExitStatus.success  # exit code for success
        elif last_test == 1:
            failed_tests += 1
            bad_inputs += 1
        else:
            failed_tests += 1

        # tests if threshold is passed for failed tests, returns relevant exit codes
        if bad_inputs >= 3:
            os.system("say access denied")
            return ExitStatus.EIO  # exit code for input/output error
        elif failed_tests >= 3:
            os.system("say access denied")
            return ExitStatus.EACCESS  # exit code for access denied
        os.system("say please try again")


if __name__ == "__main__":
    sys.exit(verify_human())
