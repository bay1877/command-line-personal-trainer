import os
import pyttsx3
from random import choice
from gtts import gTTS


engine = None

# Set TTS to the text to speech engine that you want to use.
# TTS = "GOOGLE"
TTS = "PYTTS"

def init_tts():
    """
    Initializes the pytts engine
    :return:
    """
    global engine
    engine = pyttsx3.init()

def stop_tts():
    """
    Stops the pytts engine
    :return:
    """
    global engine
    engine.stop()

def read(text):
    """
    Converts text to speech in an mp3 file 
    using google or pyttsx3.
    Plays the mp3 file.
    :param text: The rext to read
    :return:
    """
    global TTS
    if TTS == "GOOGLE":
        # Language in which you want to convert
        language = 'en'
        
        # Passing the text and language to the engine,
        # here we have marked slow=False. Which tells
        # the module that the converted audio should
        # have a high speed
        myobj = gTTS(text=text, lang=language, slow=False)
        # Saving the converted audio in a mp3 file named
        # welcome
        myobj.save("read.mp3")
        # Playing the co nverted file
        os.system("afplay read.mp3")
    elif TTS == "PYTTS":
        global engine
        engine.say(text)
        engine.runAndWait()


def read_begin():
    """
    Plays a pre-generated start sound.
    :return:
    """
    os.system("afplay begin{}.m4a".format(choice(["2", "3", "4"])))

def read_motivation():
    """
    Plays a sound clip of motivation from Kobe Bryant.
    :return:
    """
    os.popen("afplay Kobe{}.m4a".format(choice(["1", "2", "3"])))

def read_done():
    """
    Plays a pre-generated sound for when
    the user is finished with an exercise.
    :return:
    """
    os.system("afplay done{}.mp3".format(choice(["1", "2"])))




