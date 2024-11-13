import telebot
from telebot import types

bot = telebot.TeleBot('8115836051:AAG84LnSqTiGV-TjPyvDJjorJAoSfYNeAZo')

name = ''
group = ''


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "/reg":
        register(message.from_user.id, message)
    elif message.text == "/view":
        bot.send_message(message.from_user.id, f"ФИО: {name}, группа: {group}")
    else:
        bot.send_message(message.from_user.id, "send /reg")


def register(id, message):
    bot.send_message(id, "ФИО:")
    bot.register_next_step_handler(message, get_fio)


def get_fio(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Номер группы:')
    bot.register_next_step_handler(message, get_group)


def get_group(message):
    global group
    group = message.text
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text="да", callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text="нет", callback_data='no')
    keyboard.add(key_no)
    question = f'верны ли данные: ФИО: {name}, группа: {group} ?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "good .!.")
    elif call.data == "no":
        register(call.message.chat.id, call.message)


bot.polling(none_stop=True, interval=0)
