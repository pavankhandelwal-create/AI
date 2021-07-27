import pyttsx3    #pip install pyttsx3
import datetime
import speech_recognition as sr   #pip install SpeechRecognition
import smtplib
from secrets import senderemail, epwd, to
from email.message import EmailMessage, Message
import pyautogui
import webbrowser as wb
from time import sleep

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')

    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        speak("Hello this is Jarvis")

    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        speak("Hello this is Baby")
    
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S") # hour = I, min = M, sec = S
    speak("the current time is")
    speak(Time)

def date():
    date = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")

def wishme():
    speak("Welcome Back Sir!")
    time()
    date()
    greeting()
    speak("Jarvis i am here for your service,please tell me how can i help?")

def takeCommandCMD():
    quary = input("Please tell me how can i help you sir?\n")
    return quary

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizning...")
        query = r.recognize_google(audio , language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        speak("say that again Please...")
        return "None"
    return query

def sendEmail(receiver, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()

def sendwhatsmsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&test='+Message)
    sleep(10)
    pyautogui.press('enter')

if __name__ == "__main__":

    getvoices(1)
    #wishme()
    while True:
        query = takeCommandMic().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'email' in query: #we should enter password so do this and give permission for gmail
            email_list = {
                'Me': 'princekhandelwal6@gmail.com'
            }
            try:
                speak("to whom you wanna send emial!")
                name = takeCommandMic()
                receiver = email_list[name]
                speak("what is the subject of the mail?")
                subject = takeCommandMic()
                speak('what should i say?')
                content = takeCommandMic()
                sendEmail(receiver, subject, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("unable so send the mail")    #mostly it could be less secure apps is off ,so turn on.

        elif 'message' in query:
            user_name ={
                'Friday': '+91 81500 00856'
            }
            try:
                speak("to whom you wanna send the whats app message?")
                name = takeCommandMic()
                phone_no = user_name[name]
                speak("what is the message?")
                message = takeCommandMic()
                sendwhatsmsg(phone_no, message)
                speak("message has been sent")
            except Exception as e:
                print(e)
                speak("unable so send the message")
            
        elif 'bye' in query:
            quit()

