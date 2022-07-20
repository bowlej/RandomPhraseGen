import random
import webbrowser
import datetime
from gtts import gTTS
from time import sleep
import os
import pyglet
import tkinter as tk

#Setting a glabal variable to hold the choice of radio buttons on the UI
thechoice = ''

def giveMeThePhrase():
    #Create the phrase that will be either spoken and printed or just printed based on the radio button selected
    def random_phrase():
        phrase = make_me_thePhrase()
        i_need_the_date = get_the_date()
        try:
            # Check the text file to see if we already have the genrated phrase
            with open('Finscape_phrases.txt') as f:
                while phrase in f.read():
                    print('We already have that one, lets try again')
            # Adding the phrase to the file
            write_phrase_to_a_file(i_need_the_date, phrase)
        except:
            # If there is no file make one and add the phrase
            print('File to check and write phrase does not exist so will make it')
            write_phrase_to_a_file(i_need_the_date, phrase)
        if thechoice == '':
            lbl_result ["text"] = 'Silly Billy, you have not selected an option to speak the phrase or not, see the radio buttons above'
        else:
            lbl_result ["text"] = phrase


    #Making the UI
    root = tk.Tk()
    v = tk.IntVar()
    v.set(1)  # initializing the choice, i.e. Python
    fonttitles = 'Helvetica 18 bold'
    fontother = 'Helvetica 14 bold'

    #Setting the title of the UI window
    root.title('Kevs magic meetings phrase generator')
    root.geometry("950x230")

    #Making the radio button options
    speech = [("Yes", 101),
             ("No", 102)]

    #Getting the right option when radio button is selected
    def ShowChoice():
        global thechoice
        thechoice = (v.get())
        print(thechoice)
        return thechoice

    # Making the label above the radio buttons
    tk.Label(root,
             text="""Do you want to speak the phrase:""",
             font= fonttitles,
             justify = tk.CENTER,
             padx = 20).pack()

    #Creating the radio button options to show in the UI
    for choice, val in speech:
        tk.Radiobutton(root,
                       text=choice,
                       font= fontother,
                       padx = 20,
                       variable=v,
                       command=ShowChoice,
                       value=val).pack(anchor=tk.W)

    #Creating the button that will create the phrase when clicked
    btn_generate_phrase = tk.Button(
        root,
        text="Press to give phrase",
        font=fontother,
        padx = 20,
        command=random_phrase
    )
    btn_generate_phrase.pack()

    #Creating a placeholder text for where the phrase will be written
    lbl_result = tk.Label(root, text="Your phrase will appear here after pressing the button", font= fontother)
    lbl_result.pack()

    def openthepastphrases():
     filename = "Finscape_phrases.txt"
     webbrowser.open(filename)

    btn_openPastPhrasesFile = tk.Button(
        root,
        text="Press to open past phrases",
        font= fontother,
        command=openthepastphrases
    )
    btn_openPastPhrasesFile.pack()

    root.mainloop()

#Make the random phrase and speak it
def make_me_thePhrase():
    first_phrase = open('FirstPhrase.txt').read().splitlines()
    second_phrase = open('SecondPhrase.txt').read().splitlines()
    pre_phrase = 'Today i will mostly be a'
    your_phrase1 = random.choice(first_phrase)
    your_phrase2 = random.choice(second_phrase)
    finalphrase = pre_phrase + " " + your_phrase1 + " " + your_phrase2
    finalphrase.format()
    if thechoice == 101:
        speak(finalphrase)
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
    date2string = date.strftime("%d-%b-%Y")
    return date2string

#Write the results to a txt file
def write_phrase_to_a_file(date, phrase):
    print('On the {0}'.format(date) + ' ' + 'I was a {0}'.format(phrase))
    with open("Finscape_phrases.txt", mode='a') as file:
        file.write('On the {0}'.format(date) + ' ' + 'The phrase generated was : {0}'.format(phrase) + '\n')
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
