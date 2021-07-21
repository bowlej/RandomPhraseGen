import random
import datetime
from gtts import gTTS
from time import sleep
import os
import pyglet


#Do it
def random_phrase():
    phrase = make_me_thePhrase()
    i_need_the_date = get_the_date()
    try:
        #Check the text file to see if we already have the genrated phrase
        with open('Finscape_phrases.txt') as f:
            while phrase in f.read():
                print('We already have that one, lets try again')
        #Adding the phrase to the file
        write_phrase_to_a_file(i_need_the_date, phrase)
    except:
        #If there is no file make one and add the phrase
        print('File to check and write phrase does not exist so will make it')
        write_phrase_to_a_file(i_need_the_date, phrase)

#Make the random phrase
def make_me_thePhrase_with_speech_windows():
    first_phrase = open('FirstPhrase.txt').read().splitlines()
    second_phrase = open('SecondPhrase.txt').read().splitlines()
    your_phrase1 = random.choice(first_phrase)
    your_phrase2 = random.choice(second_phrase)
    finalphrase = your_phrase1 + " " + your_phrase2
    speak("I am a" + finalphrase)
    return finalphrase

def make_me_thePhrase():
    first_phrase = open('FirstPhrase.txt').read().splitlines()
    second_phrase = open('SecondPhrase.txt').read().splitlines()
    your_phrase1 = random.choice(first_phrase)
    your_phrase2 = random.choice(second_phrase)
    finalphrase = your_phrase1 + " " + your_phrase2
    return finalphrase

#Speak the random phrase
def speak(whattosay):
    tts = gTTS(text=whattosay, lang='en')
    filename = 'temp.mp3'
    tts.save(filename)
    thephrase = pyglet.media.load(filename, streaming=False)
    thephrase.play()
    sleep(thephrase.duration)  # prevent from killing 
    os.remove(filename)  # remove temperory file

#Get todays date and time
def get_the_date():
    date = datetime.datetime.now()
    date2string = date.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    return date2string

#Write the results to a txt file
def write_phrase_to_a_file(date, phrase):
    print('On the {0}'.format(date) + ' ' + 'I was a {0}'.format(phrase))
    with open("Finscape_phrases.txt", mode='a') as file:
        file.write('On the {0}'.format(date) + ' ' + 'I was a {0}'.format(phrase) + '\n')