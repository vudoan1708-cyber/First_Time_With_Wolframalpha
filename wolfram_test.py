# import a machine knowledge engine API
import wolframalpha

# import tkinter
import tkinter as tk

# text-to-speech
from gtts import gTTS
import os

# import speech recognition
# !IMPORTANT: have to install pyaudio first
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
import speech_recognition as sr

# get audio from a microphone
r = sr.Recognizer()
global recognised
recognised = False

def userSpeak():
    with sr.Microphone() as source:
        # listen to the audio
        audio = r.listen(source)
        # convert the audio into text
        try:
            global text
            text = r.recognize_google(audio)
            global recognised
            recognised = True
            if recognised == True:
                query = ''
                query = text
                # create a response
                res = client.query(query)

                answer = next(res.results).text

                # create a label
                label = tk.Label(root, text=answer)
                # print(type(answer))
                label.pack()

                # pass the language and texts into the gtts engine
                output = gTTS(text=answer, lang=lang, slow=False)
                output.save('media/output.mp3')
                os.system('start media/output.mp3')
            print(text)
        except:
            print('Sorry, could not recognise your voice')
# print('Package Loaded')
   
# define language
lang = 'en'

def getAnswer():
    # print("HEY")
    # pass
    if recognised == True:
        query = text
    else: query = entry.get()

    # create a response
    res = client.query(query)

    global answer
    answer = next(res.results).text

    # create a label
    label = tk.Label(root, text=answer)
    # print(type(answer))
    label.pack()

def speakAnswer():
    # pass the language and texts into the gtts engine
    output = gTTS(text=answer, lang=lang, slow=False)
    output.save('media/output.mp3')
    os.system('start media/output.mp3')

cv_w = 400
cv_h = 300

# create the root
root = tk.Tk()
canvas = tk.Canvas(root, width=cv_w, height=cv_h, bg='black')
canvas.pack()

# change the name of the window
root.title('AI Assistant')

# change windows icon
root.iconbitmap('media/icon/robot.ico')

# create an entry box
entry = tk.Entry(root)
canvas.create_window(cv_w / 2, cv_h / 2, window=entry)

enterBtn = tk.Button(root, text='Get the Answer', padx=20, pady=10, 
                    fg='white', bg='black', command=getAnswer)
enterBtn.pack()

speakBtn = tk.Button(root, text='Speak the Answer', padx=20, pady=10,
                    fg='white', bg='black', command=speakAnswer)
speakBtn.pack()

userSpeakBtn = tk.Button(root, text='Speak to Ask', padx=20, pady=10,
                    fg='white', bg='black', command=userSpeak)
userSpeakBtn.pack()
# ask for users input
# python v2: raw_input
# python v3: input
# input = str(input('Question: '))

# wolframalpha APP ID
APP_ID = 'WU4636-7HLUH76QPL'

# # create a client
client = wolframalpha.Client(APP_ID)

# print(answer)


root.mainloop()