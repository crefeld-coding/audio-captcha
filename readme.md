## audio-captcha Documentation

### Installation:

1. Clone or Download GitHub Repository
2. Install portaudio system wide using [homebrew](https://brew.sh/):
    * `brew install portaudio`
3. Create a venv for the project in terminal, in the project folder, run:
    * `python -m venv venv`
4. Activate the venv with:
    * `source venv/bin/activate`
5. install requirements.txt
    * `pip install -r requirements.txt`


### Running:

* First import with: 
    * `import audio-captcha`
* To run the program:
    * `verify_human()`
* You can also run the audiocaptcha file, which will run the same as running the method


### Returns:

* audiocaptcha and verify_human will return one of 3 exit codes:
    * 0 (successful exit)
    * 77 (access denied)
    * 66 (unrecognisable input)


### Bugs:

* Only works online, if it can't reach the server, the speech recognition used raises an exception


### Tips:

* If you keep getting error code 66 (unrecognisable input), try decreasing any background noise, and speaking as clearly as possible
