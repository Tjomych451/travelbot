import telebot
from telebot import types
import datetime
from datetime import datetime
import pytz
import os
from dotenv import load_dotenv

load_dotenv()



# import InlineKeyboardMarkup, InlineKeyboardButton
bot = telebot.TeleBot(os.getenv('TOKEN'))
# city= input("введи город")
@bot.message_handler(commands=['start','help'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

    btn_city = types.KeyboardButton(text="Список городов")
    btn1 = types.KeyboardButton(text="Поиск на сайте")
    btn2 = types.InlineKeyboardButton(text="Билеты")
    btn3 = types.InlineKeyboardButton(text="Погода")
    markup.add(btn_city, btn1, btn2, btn3)

    bot.send_message(message.chat.id,
                     text="{0.first_name} Я бот у которого можно узнать точную дату и время в этом городе! Можно выбрать билет на поезд. И посмотреть погоду".format(
                         message.from_user), reply_markup=markup)



@bot.message_handler()
def get_user_text(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_city = types.KeyboardButton(text="Список городов")
    btn = types.KeyboardButton(text="Меню")
    btn1 = types.InlineKeyboardButton(text="Поиск на сайте", url='https://ya.ru/')
    btn2 = types.InlineKeyboardButton(text="Билеты")
    btn3 = types.InlineKeyboardButton(text="Погода")
    markup1.add(btn_city, btn1, btn2, btn3)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(btn)
    time = datetime.now().strftime("%H:%M:%S: %A: %B")
    data = datetime.now().strftime(" %A %d  %B %Y ")
    tz_city = pytz.timezone('Europe/London')
    datetime_city = datetime.now(tz_city)

    # messa = f"Билеты для {message.from_user.first_name} здесь:"
    if message.text == "Привет" :
        bot.send_message(message.chat.id, "Привет!", parse_mode='html', reply_markup=markup1, )
    # elif message.text == "id":
    #     bot.send_message(message.chat.id, f"твой id :{message.from_user.id}", parse_mode='html')
    elif message.text == "Hello":
        bot.send_message(message.chat.id, "Привет и тебе!", parse_mode='html', reply_markup=markup1)
    elif message.text == "Время":
        bot.send_message(message.chat.id, f"Время :{time}", parse_mode='html', reply_markup=markup1)
    elif message.text == "Дата":
        bot.send_message(message.chat.id, f"Дата sd :{data}", parse_mode='html', reply_markup=markup1)
    elif message.text == "Лондон":
        bot.send_message(message.chat.id, f"Лондон :{datetime_city}", parse_mode='html',reply_markup=markup1)
    elif message.text == "Минск":
        bot.send_message(message.chat.id, f"Минск :{datetime.now(pytz.timezone('Europe/Minsk'))}", parse_mode='html',reply_markup=markup1)
    elif message.text == "Париж":
        bot.send_message(message.chat.id, f"Париж :{datetime.now(pytz.timezone('Europe/Paris'))}", parse_mode='html',reply_markup=markup1)
    elif message.text == "Саратов":
        bot.send_message(message.chat.id, f"Саратов :{datetime.now(pytz.timezone('Europe/Saratov'))}", parse_mode='html',reply_markup=markup1)
    elif message.text == "Нью-Йорк":
        bot.send_message(message.chat.id, f"Нью-Йорк :{datetime.now(pytz.timezone('America/New_York'))}", parse_mode='html',reply_markup=markup1)

    elif message.text == "Омск":
        bot.send_message(message.chat.id, f"Омск :{datetime.now(pytz.timezone('Asia/Omsk'))}", parse_mode='html',reply_markup=markup1)
    elif message.text == "Томск":
        bot.send_message(message.chat.id, f"Томск :{datetime.now(pytz.timezone('Asia/Tomsk'))}", parse_mode='html',reply_markup=markup1)
    elif message.text == "Калининград":
        bot.send_message(message.chat.id, f"Калининград :{datetime.now(pytz.timezone('Europe/Kaliningrad'))}", parse_mode='html',reply_markup=markup1)
    elif message.text == "Киев":
        bot.send_message(message.chat.id, f"Киев :{datetime.now(pytz.timezone('Europe/Kiev'))}", parse_mode='html',reply_markup=markup1)
    elif message.text == "Киров":
        bot.send_message(message.chat.id, f"Киров :{datetime.now(pytz.timezone('Europe/Kirov'))}", parse_mode='html',reply_markup=markup1)
    elif message.text == "Ульяновск":
        bot.send_message(message.chat.id, f"Ульяновск :{datetime.now(pytz.timezone('Europe/Ulyanovsk'))}", parse_mode='html',reply_markup=markup1)
    elif message.text == "Сахалин":
        bot.send_message(message.chat.id, f"Сахалин :{datetime.now(pytz.timezone('Asia/Sakhalin'))}", parse_mode='html', reply_markup=markup1)
    elif message.text == "Новосибирск":
        bot.send_message(message.chat.id, f"Новосибирск :{datetime.now(pytz.timezone('Asia/Novosibirsk'))}", parse_mode='html', reply_markup=markup1)
    elif message.text == "Магадан":
        bot.send_message(message.chat.id, f"Магадан :{datetime.now(pytz.timezone('Asia/Magadan'))}", parse_mode='html', reply_markup=markup1)
    elif message.text == "Владивосток":
        bot.send_message(message.chat.id, f"Владивосток :{datetime.now(pytz.timezone('Europe/Ulyanovsk'))}", parse_mode='html', reply_markup=markup1)


    elif message.text == "Поиск на сайте":
        # bot.send_message(message.chat.id, "Привет и тебе!", parse_mode='html')
        # markup.add(types.InlineKeyboardButton('Поиск на сайте', url="https://ya.ru/"))
        # types.InlineKeyboardButton(text="Поиск на сайте", url="ya.ru", reply_markup=markup)
        bot.send_message(message.chat.id, "https://ya.ru/", parse_mode='html', reply_markup=markup1)
    elif message.text == "Погода":
        bot.send_message(message.chat.id, "https://m.rp5.ru/", parse_mode='html')

        bot.send_message(message.chat.id, "https://ya.ru/pogoda/rostov-na-donu", parse_mode='html', reply_markup=markup1)

    elif message.text == "Билеты":
        bot.send_message(message.from_user.id, "https://rzd.ru/", reply_markup=markup )
    elif message.text == "Меню":
        bot.send_message(message.from_user.id,"Меню", parse_mode='html', reply_markup=markup1 )
    elif message.text == "Список городов":
        bot.send_message(message.from_user.id, "Владивосток, Калининград, Киев, Киров, Лондон, Магадан,Минск, Новосибирск, Нью-Йорк,Омск,Париж, Саратов, Сахалин, Томск,Ульяновск", reply_markup=markup )
    else:
        bot.send_message(message.chat.id, "НЕТ такой команды или ошибка при вводе", parse_mode='html', reply_markup=markup1)

# @bot.message_handler(commands=['Повторюшка'])
# def handle_message(message):
#     markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     bot.reply_to(message,'from_user.id' + message.text, reply_markup=markup2 )
#
#     btn = types.KeyboardButton(text="меню")
#     markup2.add(btn)



bot.polling(none_stop=True)