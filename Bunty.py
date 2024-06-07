import pyttsx3
import speech_recognition as sr
from datetime import date
import time
import webbrowser
import datetime
from pynput.keyboard import Key, Controller
import pyautogui
import sys
import os
from os import listdir
from os.path import isfile, join
import smtplib
import wikipedia
import Gesture_Controller
import app
from threading import Thread
import cv2
import openai  

today = date.today()
r = sr.Recognizer()
keyboard = Controller()
engine = pyttsx3.init('sapi5')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


file_exp_status = False
files = []
path = ''
is_awake = True

def reply(audio):
    app.ChatBot.addAppMsg(audio)
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        reply("Good Morning!")
    elif 12 <= hour < 18:
        reply("Good Afternoon!")
    else:
        reply("Good Evening!")

    reply("Welcome back Jaya Bhanu Prakash sir! This is Bunty!!")

with sr.Microphone() as source:
        r.energy_threshold = 500 
        r.dynamic_energy_threshold = False


def record_audio():
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        voice_data = ''
        audio = r.listen(source, phrase_time_limit=5)

        try:
            voice_data = r.recognize_google(audio)
        except sr.RequestError:
            reply('Sorry my Service is down. Please check your Internet connection')
        except sr.UnknownValueError:
            print('cannot recognize')
            pass
        return voice_data.lower()
    
def open_camera():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = cap.read()

        cv2.imshow("Camera", frame)
        if 'open camera' in voice_data or 'start camera' in voice_data:
            print("Opening camera...")
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def respond(voice_data):
    global file_exp_status, files, is_awake, path
    print(voice_data)
    voice_data.replace('bunty', '')
    app.eel.addUserMsg(voice_data)

    if is_awake == False:
        if 'wake up' in voice_data:
            is_awake = True
            wish()

    elif 'hello' in voice_data:
        wish()

    elif 'what is your name' in voice_data:
        reply('Bunty! Thanks for Asking')

   
    elif 'who is your boss' in voice_data:
        reply('Mr. Jaya Bhanu Prakash M')  
        
    elif 'Who is the CEO of Semonical' in voice_data:
        reply('Mr. Jaya Bhanu Prakash Murapaka')    

    elif 'when was your birthdate' in voice_data:
        reply('April 20, 2022')


    elif 'prepare ppt for machine learning' in voice_data:
          pyautogui.press('win')
          time.sleep(1)
          pyautogui.write('powerpoint')
          time.sleep(1)
          pyautogui.press('enter')
          time.sleep(1)
          pyautogui.press('enter')
          time.sleep(2)
          pyautogui.write('Why You are Paying fees for college and asking me Go and Prepare Yourself')  
          reply('got it right.....go and make by your self') 
   
    elif 'date' in voice_data:
        reply(today.strftime("%B %d, %Y"))

    elif 'time' in voice_data:
        reply(str(datetime.datetime.now()).split(" ")[1].split('.')[0])

    elif ('hotstar' in voice_data) or ('disney plus hotstar' in voice_data) or ('disney' in voice_data) or ('open disney plus hotstar' in voice_data):
        reply('Opening Disney Plus Hotstar')
        url = 'https://www.hotstar.com/in/home'
        try:
            webbrowser.get().open(url)
            reply('Opened Disney Plus Hotstar')
        except:
            reply('Please Check Your Internet')

    elif ('Amazon Prime' in voice_data) or ('prime video' in voice_data) or ('amazon prime video' in voice_data) or ('open amazon prime' in voice_data):
         reply('opening Amazon Prime Video')   
         url = 'https://www.primevideo.com/' 
         try:
            webbrowser.get().open(url)
            reply('This is what I found Sir')
         except:
            reply('Please check your Internet')

    elif 'download chrome'in voice_data:
         reply('Downloading Chrome')   
         url = 'https://www.google.com/chrome/next-steps.html?brand=CHBD&statcb=0&installdataindex=empty&defaultbrowser=0#' 
         try:
            webbrowser.get().open(url)
            reply('Download started')
         except:
            reply('Please check your Internet')

    elif ('tech telugu knowledge'in voice_data) or ('Take telugu Knowledge' in voice_data) or ('open my youtube channel' in voice_data) or ('Tech Telugu Knowledge' in voice_data):
         reply('Opening Your YouTube Channel sir')   
         url = 'https://www.youtube.com/@TechTeluguKnowledge' 
         try:
            webbrowser.get().open(url)
            reply('Opened Your YouTube Channel First Contineous gha videos cheyyii Bey')
         except:
            reply('Please check your Internet')        

    elif ('Netflix' in voice_data) or ('Netuflix' in voice_data) or ('open netflix' in voice_data): 
         reply('opening Netflix')   
         url = 'https://www.netflix.com/in/' 
         try:
            webbrowser.get().open(url)
            reply('This is what I found Sir')
         except:
            reply('Please check your Internet')

    elif ('search' in voice_data) or ('such' in voice_data) or ('sach' in voice_data):
        reply('what are you looking for ?')
        temp_audio = record_audio()
        app.eel.addUserMsg(temp_audio)
        reply('Searching for ' + voice_data.split('search')[1])
        url = 'https://google.com/search?q=' +  temp_audio + '&amp;'
        try:
            webbrowser.get().open(url)
            reply('This is what I found Sir')
        except:
            reply('Please check your Internet')

    elif 'location' in voice_data:
        reply('Which place are you looking for ?')
        temp_audio = record_audio()
        app.eel.addUserMsg(temp_audio)
        reply('Locating...')
        url = 'https://google.nl/maps/place/' + temp_audio + '/&amp;'
        try:
            webbrowser.get().open(url)
            reply('This is what I found Sir')
        except:
            reply('Please check your Internet')

    elif 'delete temporary files' in voice_data:
        try:
         with keyboard.pressed(Key.cmd):
            keyboard.press('r')
            keyboard.release('r')

         time.sleep(1)

         pyautogui.write('%temp%')
         pyautogui.press('enter')

         time.sleep(2)

         with keyboard.pressed(Key.ctrl):
            keyboard.press('a')
            keyboard.release('a')

         keyboard.press(Key.delete)
         keyboard.release(Key.delete)

         time.sleep(1)
         keyboard.press(Key.enter)
         keyboard.release(Key.enter)

         reply('Temporary files deleted successfully.')
        except:
         reply(f'An error occurred: {str(e)}')

    elif 'restart system' in voice_data:
        try:
            os.system('shutdown /r /t 1')
        except:
         reply(f'An error occurred: {str(e)}')

    elif ('shutdown system' in voice_data) or ('stutdown' in voice_data) or ('destroy yourself' in voice_data) or ('2.0' in voice_data) or ('i am done' in voice_data) or ('Im done' in voice_data) or ('its time to take rest' in voice_data):
        try:
            os.system('shutdown /s /t 1')
        except:
         reply(f'An error occurred: {str(e)}')

    elif 'why this kolaveri' in voice_data:
        reply('Yo boys i am singing song.......Soup song........Flop song..................Why this kolaveri kolaveri kolaveri di............Why this kolaveri kolaveri kolaveri di.........Rhythm correct..........Why this kolaveri kolaveri kolaveri di...............Maintain please............Why this kolaveri….ah di')

    elif ('sleep system' in voice_data) or ('sleep' in voice_data) or ('paduko' in voice_data) or ('suijavyu' in voice_data) or ('sona' in voice_data): 
        try:
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
        except:
         reply(f'An error occurred: {str(e)}')

    elif ('bye' in voice_data) or ('by' in voice_data):
        reply("Goodbye! Exiting the application.")
        app.ChatBot.close()
        sys.exit()
        is_awake = False

    elif ('exit' in voice_data) or ('terminate' in voice_data):
        if Gesture_Controller.GestureController.gc_mode:
            Gesture_Controller.GestureController.gc_mode = 0
        app.ChatBot.close()
        sys.exit()
         
    
    elif 'launch gesture recognition' in voice_data:
        if Gesture_Controller.GestureController.gc_mode:
            reply('Gesture recognition is already active')
        else:
            gc = Gesture_Controller.GestureController()
            t = Thread(target = gc.start)
            t.start()
            reply('Launched Successfully')

    elif ('stop gesture recognition' in voice_data) or ('top gesture recognition' in voice_data):
        if Gesture_Controller.GestureController.gc_mode:
            Gesture_Controller.GestureController.gc_mode = 0
            reply('Gesture recognition stopped')
        else:
            reply('Gesture recognition is already inactive')

    elif 'select the data' in voice_data:
        with keyboard.pressed(Key.ctrl):
            keyboard.press('a')
            keyboard.release('a')
        reply('Selected the data from the screen')

    elif 'Open CMD' in voice_data or 'open cmd' in voice_data or 'cmd' in voice_data or 'commad prompt' in voice_data:
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.write('cmd')
        time.sleep(2)
        pyautogui.press('enter')
        reply('Done')

    elif 'send message to bunty on whatsapp'in voice_data:
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.write('whatsapp')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('down')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write('Hi This is Bunty and You are also bunty, why you asked me to message you')
        time.sleep(2)
        pyautogui.press('enter')
        reply('message done')

    elif 'send message to bhavin on whatsapp'in voice_data:
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.write('whatsapp')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write('bhavin')
        time.sleep(2)
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('enter')
        pyautogui.write('Hi Bhavin How are you')
        time.sleep(2)
        pyautogui.press('enter')
        reply('message done')

    elif 'send message to varun on whatsapp'in voice_data:
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.write('whatsapp')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write('varun')
        time.sleep(2)
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('enter')
        pyautogui.write('Hi varun this is bunty, Bhanu wants to message you....nee pakkane unadu ga malli enduku message cheyamandu velli vadiki chepu')
        time.sleep(2)
        pyautogui.press('enter')
        reply('message done')

    elif 'copy' in voice_data:
        with keyboard.pressed(Key.ctrl):
            keyboard.press('c')
            keyboard.release('c')
        reply('Copied')

    elif 'open notepad' in voice_data or 'notepad' in voice_data or 'open something to write' in voice_data:
         
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.write('notepad')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        reply('Opened Notepad')


    elif 'open camera' in voice_data or 'camera' in voice_data or 'open something to take picture' in voice_data:
         
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.write('camera')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        reply('Opened camera')

    elif 'change mode to photo' in voice_data:
          pyautogui.press('down')
    elif ' change mode to video' in voice_data:
          pyautogui.press('up')
          reply('mode changed')
    elif 'take picture' in voice_data or 'record video' in voice_data:
          pyautogui.press('space')
          reply('done')

    elif 'page' in voice_data or 'pest'  in voice_data or 'paste' in voice_data:
        with keyboard.pressed(Key.ctrl):
            keyboard.press('v')
            keyboard.release('v')
        reply('Pasted')
        
    elif 'list' in voice_data:
        counter = 0
        path = 'C://'
        files = listdir(path)
        filestr = ""
        for f in files:
            counter+=1
            print(str(counter) + ':  ' + f)
            filestr += str(counter) + ':  ' + f + '<br>'
        file_exp_status = True
        reply('These are the files in your root directory')
        app.ChatBot.addAppMsg(filestr)
        
    elif file_exp_status == True:
        counter = 0   
        if 'open' in voice_data:
            if isfile(join(path,files[int(voice_data.split(' ')[-1])-1])):
                os.startfile(path + files[int(voice_data.split(' ')[-1])-1])
                file_exp_status = False
            else:
                try:
                    path = path + files[int(voice_data.split(' ')[-1])-1] + '//'
                    files = listdir(path)
                    filestr = ""
                    for f in files:
                        counter+=1
                        filestr += str(counter) + ':  ' + f + '<br>'
                        print(str(counter) + ':  ' + f)
                    reply('Opened Successfully')
                    app.ChatBot.addAppMsg(filestr)
                    
                except:
                    reply('You do not have permission to access this folder')
                                    
        if 'back' in voice_data:
            filestr = ""
            if path == 'C://':
                reply('Sorry, this is the root directory')
            else:
                a = path.split('//')[:-2]
                path = '//'.join(a)
                path += '//'
                files = listdir(path)
                for f in files:
                    counter+=1
                    filestr += str(counter) + ':  ' + f + '<br>'
                    print(str(counter) + ':  ' + f)
                reply('ok')
                app.ChatBot.addAppMsg(filestr)


t1 = Thread(target = app.ChatBot.start)
t1.start()

while not app.ChatBot.started:
    time.sleep(0.5)

wish()
voice_data = None
while True:
    if app.ChatBot.isUserInput():
        voice_data = app.ChatBot.popUserInput()
    else:
        voice_data = record_audio()
    if 'bunty' in voice_data:
        try:
            respond(voice_data)
        except SystemExit:
            reply("Exit Successful")
            break
        except:
            print("EXCEPTION raised while closing.")
            break
        
        
