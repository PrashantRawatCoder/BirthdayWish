import time
from datetime import datetime
import sys
from colorama import Fore, Back, Style
import smtplib
import art
import imghdr
from email.message import EmailMessage

def intro():
    print(Fore.RED+"===================================="*4+Fore.GREEN+art.text2art("\n\nWish \n                    Birthday\nAutomatic\n\n")+Fore.RED+"===================================="*4+"\nBy LearnEHKing")
    print(Style.RESET_ALL)

def outro():
    intro()
    print(Fore.MAGENTA+"Thanks fir using Automatic Birthday Wisher .")
    print(Style.RESET_ALL)
    exit()


def sendmail(frommail,password,to,sub,msg,name="name"):
    wish1="""                       ,
                     (_)
                      |-|
                      | |
                      | |
                     .| |.
                    |'---'|
                  |~  ~~|
             .-@'|  ~  |'@-.
            (@    '---'    @)
          |'-@..__@__..@-'|
       () |~  ~ ~ ~     ~ | ()
       {||'| ~() ~   ~ ()~ |'||}
     ( || @'-||.__~__.||-'@ || )
     |'-....__  ||   @   ||  __...-'|
     |~ ~  '''--------------'''  ~ ~|
   |  ~  ~ H A P P Y ~ ~  ~|
   | ~  B I R T H D A Y ~ ~ |
   '-..._By LearnEHKing_...-'

          '''---------'''
May your sweet smile never fade away.
I wish you a very happy and sweet birthday.
Good bless you."""
    
    wish2=""" 
                          0     0
                           |      |
                    ____|___|____
               0  |~ ~ ~ ~ ~ ~|   0
                     |  |           |   |
          ___|__|___________|___|__
           |/\/\/\/\/\/\/\/\/\/\/\/|
          0   |       H a p p y       |   0
       |   |/\/\/\/\/\/\/\/\/\/\/\/|   |
 _|___|_______________________|___|__
   |/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|
   |                                                          |
   |               B i r t h d a y! ! !                 |
  | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |
|___________________________________|



\nMay you achieve everything you desire in life.\nI wish you a very sweet and happy birthday.\nMay you have an awesome life ahead.\nEnjoy your day"""
    message=str(wish1+"\n\n\n\n\n"+wish2+"\n\n\n\n\n")
    for i in range(len(msg[0])):
        message=str(message+msg[0][i])+"\n\n\n\n\n\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"*2+"\n\n\n\n"
    
    
    newMessage = EmailMessage()                         
    newMessage['Subject'] = sub
    newMessage['From'] = frommail                 
    newMessage['To'] = to               
    newMessage.set_content(message)
    if msg[1]!=[]:
        for img in msg[1]:
            with open(img, 'rb') as f:
                image_data = f.read()
                image_type = imghdr.what(f.name)
                image_name = f.name
            newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login(frommail,password)
        smtp.send_message(newMessage)
 
def sendmailtime(time,date,frommail,password,tomail,sub,msgl,hmt,name):
    
    
    print("Your email will send at ",time ," ",date)
    print("Started at : "+ datetime.now().strftime("%I:%M%p")+" "+datetime.now().strftime("%d-%m-%Y"))
    while True :
        
        if date==datetime.now().strftime("%d-%m-%Y"):
            while True:
                if time==datetime.now().strftime("%I:%M%p"):
                        print(Fore.BLUE+"Sending Mail.....")
                        for i in range (hmt):
                            sendmail(frommail,password,tomail,sub,msgl,name)
                            print(Fore.GREEN+"Email Sended ",i+1,"times...")
                        print("Email Successfully Sent .....")
                        outro()
                        break


if __name__ == "__main__":
    try :
        intro()
        paralist=[]
        imglist=[]
        print(Fore.MAGENTA+"\nEnter Name Of Person Whose Birthday is :"+Fore.YELLOW)
        name=input("$ : ")
        print(Fore.MAGENTA+"\nEnter Two Digit Date (only Day) of Birthday Without space (Ex. 01) :"+Fore.YELLOW)
        date1=input("$ : ")
        print(Fore.MAGENTA+"\nEnter Two Digit Month (only Month) of Birthday Without space (Ex. 06) :"+Fore.YELLOW)
        date2=input("$ : ")
        print(Fore.MAGENTA+"\nEnter Four Digit Year (only year) of Birthday Without space (Ex. 2021) :"+Fore.YELLOW)
        date3=input("$ : ")
        print(Fore.MAGENTA+"\nEnter Two Digit Hour for sending email Without space (Ex. 12) :"+Fore.YELLOW)
        time1=input("$ : ")
        print(Fore.MAGENTA+"\nEnter Two Digit Minutes for sending email Without space (Ex. 01) :"+Fore.YELLOW)
        time2=input("$ : ")
        print(Fore.MAGENTA+"\nEnter AM/PM for sending email Without space (Ex. AM) :"+Fore.YELLOW)
        time3=input("$ : ")
        print(Fore.MAGENTA+"\nEnter Email Of Person Whose Birthday is :"+Fore.YELLOW)
        tomail=input("$ : ")
        print(Fore.MAGENTA+"\nEnter Your email (For sending to your Friend) :"+Fore.YELLOW)
        frommail=input("$ : ")
        print(Fore.MAGENTA+"\nEnter Your email Password (For sending to your Friend) :"+Fore.YELLOW)
        password=input("$ : ")
        print(Fore.MAGENTA+"\nEnter mail subject (Ex. : Happy Birthday):"+Fore.YELLOW)
        sub=input("$ : ")
        print(Fore.MAGENTA+"\nEnter How many time you want to send mail to your friend:"+Fore.YELLOW)
        hmt=int(input("$ : "))
        print(Fore.MAGENTA+"\nEnter How Many Picture You want to send (0 for no picture)"+Fore.YELLOW)
        hmimg=int(input("$ : "))
        print(Fore.MAGENTA+"\nEnter How many Paragrapha you want to send (minimum = 1) :"+Fore.YELLOW)
        hmpara=int(input("$ : "))
        
        for i in range(hmpara):
            print(Fore.MAGENTA+f"\nEnter Your Para (Count : {i+1}):"+Fore.YELLOW)
            paralist.append(input("$ : "))
        for i in range(hmimg):
            print(Fore.MAGENTA+f"\nEnter Path of Image {i+1} :"+Fore.YELLOW)
            imglist.append(input("$ : "))
        msgl=[paralist,imglist]
        
        date =str(date1)+"-"+str(date2)+"-"+str(date3)
        time = str(time1)+":"+str(time2)+time3.upper()
        print(Style.RESET_ALL)
        
        sendmailtime(time,date,frommail,password,tomail,sub,msgl,hmt,name)
    except Exception as error:
        print(Fore.RED)
        print("An Error occure : ", error)
        print("Retry .")
        print(Style.RESET_ALL)