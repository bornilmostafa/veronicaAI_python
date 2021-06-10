import datetime
import subprocess as s
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia

listener = sr.Recognizer()
veronica = pyttsx3.init()
voices = veronica.getProperty('voices')
veronica.setProperty('voice', voices[1].id)


def talk(text):
    veronica.say(text)
    veronica.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listing......')

            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'veronica' in command:
                command = command.replace('veronica', '')
                print(command)
    except:
        pass
    return command


def run_veronica():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%S %p ')
        print(time)
        talk('Current Time is : ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('PLaying...' + song)
        pywhatkit.playonyt(song)
    elif 'Tell me about' in command:
        look_for = command.replace('Tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)
    elif 'Joke' in command:
        talk(pyjokes.get_jokes())
    elif 'date' in command:
        talk('Sorry,I am a AI which is created by my boss Bornil Mostafa')
    elif 'Cisco' in command:
        s.Popen("D:\\Program Files\\Cisco Packet Tracer 8.0\\bin\\PacketTracer.exe")

    else:
        talk('I did not get it but I can search it for you')
        pywhatkit.search(command)


while True:
    run_veronica()
