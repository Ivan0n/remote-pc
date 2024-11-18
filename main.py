import telebot
from tkinter.messagebox import showinfo, askyesno
import os
import webbrowser
import pyscreenshot

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
    bot.send_message(sys32.chat.id,'🌵Меню system32🌵 \n ☀️explorer - /explorer \n ☀️calc /calc \n ☀️Спящий режим /sleep \n ☀️Блокировка пк /block \n ☀️Перезагрузка пк /restart_pc \n ☀️Выключение пк /off_pc')
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
        try:
            bot.send_message(calcul.chat.id, 'Запуск второй версии калькулятора')
            os.startfile(r'C:\Windows\System32\calc.exe')
        except:
            bot.send_message(calcul.chat.id, 'Не удалось найти вторую версию, ищем первую!!! ')

            try:
                os.startfile(r'C:\Windows\System32\win32calc.exe')
                bot.send_message(calcul.chat.id, 'Запуск первой версии калькулятора')
            except:
                bot.send_message(calcul.chat.id, 'Извените, ошибка!!!')
    else:
        bot.send_message(calcul.chat.id, '✋Хост не подключен✋ \n Воспользуйтесь командой /connect')
@bot.message_handler(commands=['sleep'])
def sleep(sleeper):
    cheker = open('connect.txt')
    value = int(cheker.readline())
    if value == 1:
        bot.send_message(sleeper.chat.id, 'Спящий режим')
        os.startfile(r'sleep.lnk')

    else:
        bot.send_message(sleeper.chat.id, '✋Хост не подключен✋ \n Воспользуйтесь командой /connect')
@bot.message_handler(commands=['block'])
def block(blocker):
    cheker = open('connect.txt')
    value = int(cheker.readline())
    if value == 1:
        bot.send_message(blocker.chat.id, 'Спящий режим')
        os.startfile(r'block.lnk')

    else:
        bot.send_message(blocker.chat.id, '✋Хост не подключен✋ \n Воспользуйтесь командой /connect')
@bot.message_handler(commands=['off_pc'])
def off(offer):
    cheker = open('connect.txt')
    value = int(cheker.readline())
    if value == 1:
        bot.send_message(offer.chat.id, 'Выключение!!! Программа после выключения работать не будет!!!')
        os.startfile(r'off.lnk')

    else:
        bot.send_message(offer.chat.id, '✋Хост не подключен✋ \n Воспользуйтесь командой /connect')
@bot.message_handler(commands=['restart_pc'])
def off(offer):
    cheker = open('connect.txt')
    value = int(cheker.readline())
    if value == 1:
        bot.send_message(offer.chat.id, 'Перезагрузка!!! Программа после перезагрузки работать не будет!!!')
        os.startfile(r'restart.lnk')

    else:
        bot.send_message(offer.chat.id, '✋Хост не подключен✋ \n Воспользуйтесь командой /connect')
@bot.message_handler()
def none(none):
    bot.send_message(none.chat.id, '<em>Неизвестная команда</em> \n попробуйте написать /help ', parse_mode='html')

bot.polling(non_stop=True)