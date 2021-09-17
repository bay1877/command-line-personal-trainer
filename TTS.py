import os
import pyttsx3
from random import choice


engine = None


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
    global engine
    engine.say(text)
    engine.runAndWait()


def read_begin():
    """
    Plays a pre-generated start sound.
    :return:
    """
    os.system("afplay ./audiofiles/begin{}.m4a".format(choice(["2", "3", "4"])))