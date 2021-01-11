import pyttsx3
import speech_recognition as sr


text = "Hello Mr. Gold"

# Setup lloyd
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Lloyd speak function
def lloyd_speak():
    engine.say(text)
    engine.runAndWait()
lloyd_speak()

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))