import telebot
from tkinter.messagebox import showinfo, askyesno
from tkinter import ttk
from mouseinfo import screenshot
from pyexpat.errors import messages
from pymsgbox import password
from telebot import types
import os
import webbrowser
import pyscreenshot
from telebot import types

token_txt = open('bot_token.txt')
bot_token = str(token_txt.readline())

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start' , 'connect'])

def start(starter):
    cheker = open('connect.txt')
    value = int(cheker.readline())
    if value == 0:
        bot.send_message(starter.chat.id, '🍀Подтвердите доступ к боту на вашем устройстве🍀')
        result = askyesno(title="Подтвержение подключения", message="Соедениться с ботом??? Token: " + bot_token)
        if result:
            cheker = open('connect.txt')
            value = int(cheker.readline())
            print(value)
            if value == 0:
                with open("connect.txt", "w+") as f:
                    f.write("1")
                bot.send_message(starter.chat.id, '✅Хост подключен✅')
            else:
                bot.send_message(starter.chat.id, '✋Хост уже подключен✋')

        else:
            bot.send_message(starter.chat.id, '❌Ваш доступ разорван хостом❌')
            showinfo(title="Соединение разорвано", message="Вы отклонили подключение!!!")
    else:
        bot.send_message(starter.chat.id, '✋Хост уже подключен✋ \n Воспользуйтесь командой /help')

@bot.message_handler(commands=['help'])
def help(helper):
    bot.send_message(helper.chat.id, '🌵Меню комманд🌵 \n ☀️Раздел - /system32 \n ☀️Открыть ссылку - /browser \n ☀️Действия - /mvs')

@bot.message_handler(commands=['mvs'])
def mvs(moves):
    bot.send_message(moves.chat.id,'🌵Меню Действий🌵 \n ☀️Скриншот - /screen \n ☀️Запустить программу /programm_start')
@bot.message_handler(commands=['system32'])
def system(sys32):
    bot.send_message(sys32.chat.id,'🌵Меню system32🌵 \n ☀️explorer - /explorer \n ☀️calc /calc')
@bot.message_handler(commands=['browser'])
def broser(browser):
    bot.send_message(browser.chat.id, '🌵Меню browser🌵 \n ☀️YouTube - /yt \n ☀️VK /vk')
@bot.message_handler(commands=['yt'])
def YouTube(yt):
    cheker = open('connect.txt')
    value = int(cheker.readline())
    if value == 1:
        bot.send_message(yt.chat.id, 'Запуск YouTube')
        webbrowser.open('https://www.youtube.com/')
    else:
        bot.send_message(yt.chat.id, '✋Хост не подключен✋ \n Воспользуйтесь командой /connect')
@bot.message_handler(commands=['screen'])
def screen(shoter):
    cheker = open('connect.txt')
    value = int(cheker.readline())
    if value == 1:
        bot.send_message(shoter.chat.id, 'Скриншот будет сохранён в директории с файлом ')
        image = pyscreenshot.grab()
        image.save("screenshot.png")
        photo = open('screenshot.png', 'rb')
        bot.send_photo(shoter.chat.id, photo)
    else:
        bot.send_message(shoter.chat.id, '✋Хост не подключен✋ \n Воспользуйтесь командой /connect')

@bot.message_handler(commands=['explorer'])
def expl(explorer):
    cheker = open('connect.txt')
    value = int(cheker.readline())
    if value == 1:
        bot.send_message(explorer.chat.id, 'Запуск explorer')
        os.startfile(r'C:\Windows\explorer.exe')
    else:
        bot.send_message(explorer.chat.id, '✋Хост не подключен✋ \n Воспользуйтесь командой /connect')
@bot.message_handler(commands=['calc'])
def calc(calcul):
    cheker = open('connect.txt')
    value = int(cheker.readline())
    if value == 1:
        bot.send_message(calcul.chat.id, 'Запуск calc')
        os.startfile(r'C:\Windows\System32\win32calc.exe')
    else:
        bot.send_message(calcul.chat.id, '✋Хост не подключен✋ \n Воспользуйтесь командой /connect')
@bot.message_handler()
def none(none):
    bot.send_message(none.chat.id, '<em>Неизвестная команда</em> \n попробуйте написать /help ', parse_mode='html')

bot.polling(non_stop=True)