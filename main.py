import os
from telebot import *
import platform
import psutil
import webbrowser
import pyautogui
import keyboard

API_TOKEN = ''
user_id=''#при запуске он говорить твой id
bot = telebot.TeleBot(API_TOKEN)






@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('ПК 💻')
    item2 = types.KeyboardButton('открыть')
    item3 = types.KeyboardButton('мультимедия')
    item4 = types.KeyboardButton('отключить код')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, message.from_user.id, reply_markup=markup)

@bot.message_handler(content_types=['text'])

def bot_message(message):
    if message.chat.type == 'private':
        if message.from_user.id == user_id:
            if message.text == 'ПК 💻':

                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('выключить')
                item2 = types.KeyboardButton('Назад ⬅')
                item3 = types.KeyboardButton('перезапуск')
                item4 = types.KeyboardButton('сон')
                item5 = types.KeyboardButton('инфо')
                item6 = types.KeyboardButton('нагрузка')
                item7 = types.KeyboardButton('скриншот')
                markup.add(item1, item2, item3, item4, item5, item6, item7)
                bot.send_message(message.chat.id, 'ПК 💻', reply_markup=markup)
            elif message.text == 'Назад ⬅':

                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('ПК 💻')
                item2 = types.KeyboardButton('открыть')
                item3 = types.KeyboardButton('мультимедия')
                item4 = types.KeyboardButton('отключить код')
                markup.add(item1, item2, item3, item4)
                bot.send_message(message.chat.id, 'Назад ⬅', reply_markup=markup)
            elif message.text == 'выключить':

                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                item2 = types.KeyboardButton('открыть')
                item1 = types.KeyboardButton('ПК 💻')
                item3 = types.KeyboardButton('мультимедия')
                item4 = types.KeyboardButton('отключить код')
                markup.add(item1, item2, item3, item4)
                bot.send_message(message.chat.id, 'Выключаю...', reply_markup=markup)
                os.system("shutdown /s /t 0")
            elif message.text == 'перезапуск':


                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                item2 = types.KeyboardButton('открыть')
                item1 = types.KeyboardButton('ПК 💻')
                item3 = types.KeyboardButton('мультимедия')
                item4 = types.KeyboardButton('отключить код')
                markup.add(item1, item2, item3, item4)
                bot.send_message(message.chat.id, 'Презагружаю...', reply_markup=markup)
                os.system("shutdown /r /t 0")
            elif message.text == 'сон':

                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                item2 = types.KeyboardButton('открыть')
                item1 = types.KeyboardButton('ПК 💻')
                item3 = types.KeyboardButton('мультимедия')
                item4 = types.KeyboardButton('отключить код')
                markup.add(item1, item2, item3, item4)
                bot.send_message(message.chat.id, 'Сплю...', reply_markup=markup)
                os.system("shutdown /h")
            elif message.text == 'инфо':

                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('ПК 💻')
                item2 = types.KeyboardButton('открыть')
                item3 = types.KeyboardButton('мультимедия')
                item4 = types.KeyboardButton('отключить код')
                markup.add(item1, item2, item3, item4)
                info = {}
                platform_details = platform.platform()
                info["platform details"] = platform_details
                system_name = platform.system()
                info["system name"] = system_name
                processor_name = platform.processor()
                info["processor name"] = processor_name
                architecture_details = platform.architecture()
                info["architectural detail"] = architecture_details
                pc_info = []
                for i, j in info.items():
                    bot.send_message(message.chat.id, i + " - " + j)
                bot.send_message(message.chat.id, 'ПК 💻', reply_markup=markup)
                markup.add(item1)
            elif message.text == 'нагрузка':

                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('ПК 💻')
                item2 = types.KeyboardButton('открыть')
                item3 = types.KeyboardButton('мультимедия')
                item4 = types.KeyboardButton('отключить код')
                markup.add(item1, item2, item3, item4)
                bot.send_message(message.chat.id, 'GPU :')
                bot.send_message(message.chat.id,psutil.cpu_percent(4))
                bot.send_message(message.chat.id, 'ПК 💻', reply_markup=markup)
            elif message.text == 'открыть':
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('URL')
                item2 = types.KeyboardButton('Назад ⬅')
                item3 = types.KeyboardButton('открыть exe')
                markup.add(item1, item2, item3)
                bot.send_message(message.chat.id, 'открыть', reply_markup=markup)
            elif message.text[:6] == 'URL':
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('ПК 💻')
                item2 = types.KeyboardButton('открыть')
                item3 = types.KeyboardButton('мультимедия')
                item4 = types.KeyboardButton('отключить код')
                markup.add(item1, item2, item3, item4)
                webbrowser.open_new_tab(message.text)
                bot.send_message(message.chat.id, 'Открываю URL', reply_markup=markup)
            elif message.text == 'открыть exe':
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('ПК 💻')
                item2 = types.KeyboardButton('открыть')
                item3 = types.KeyboardButton('мультимедия')
                item4 = types.KeyboardButton('отключить код')
                markup.add(item1, item2, item3, item4)
                os.system('"C:/Windows/System32/notepad.exe"')
                bot.send_message(message.chat.id, 'Открываю exe', reply_markup=markup)
            elif message.text == 'скриншот':
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('ПК 💻')
                item2 = types.KeyboardButton('открыть')
                item3 = types.KeyboardButton('мультимедия')
                item4 = types.KeyboardButton('отключить код')
                markup.add(item1, item2, item3, item4)
                im2 = pyautogui.screenshot('s.png')
                bot.send_photo(message.chat.id, photo=open('s.png', 'rb'))
                bot.send_message(message.chat.id, 'Скриншот', reply_markup=markup)
            elif message.text == 'мультимедия':
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('⬅')
                item2 = types.KeyboardButton('⏯')
                item3 = types.KeyboardButton('➡')
                item4 = types.KeyboardButton('Назад ⬅')
                markup.add(item1, item2, item3, item4)
                bot.send_message(message.chat.id, 'мультимедия', reply_markup=markup)
            elif message.text == '➡':
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('⬅')
                item2 = types.KeyboardButton('⏯')
                item3 = types.KeyboardButton('➡')
                item4 = types.KeyboardButton('Назад ⬅')
                markup.add(item1, item2, item3, item4)
                keyboard.send("right")
                bot.send_message(message.chat.id, '⬅', reply_markup=markup)
            elif message.text == '⏯':
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('⬅')
                item2 = types.KeyboardButton('⏯')
                item3 = types.KeyboardButton('➡')
                item4 = types.KeyboardButton('Назад ⬅')
                markup.add(item1, item2, item3, item4)
                keyboard.send("space")
                bot.send_message(message.chat.id, '⏯', reply_markup=markup)
            elif message.text == '⬅':
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('⬅')
                item2 = types.KeyboardButton('⏯')
                item3 = types.KeyboardButton('➡')
                item4 = types.KeyboardButton('Назад ⬅')
                markup.add(item1, item2, item3, item4)
                keyboard.send("left")
                bot.send_message(message.chat.id, '➡', reply_markup=markup)
            elif message.text == 'отключить код':
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('ПК 💻')
                item2 = types.KeyboardButton('открыть')
                item3 = types.KeyboardButton('мультимедия')
                item4 = types.KeyboardButton('отключить код')
                markup.add(item1, item2, item3, item4)
                bot.send_message(message.chat.id, 'отключаю... меню больше не работает', reply_markup=markup)
                exit(0)


bot.infinity_polling()
