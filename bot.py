# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(regexp="id")
def handle_start_help(message):
    print(message.chat.id)
    pass

@bot.message_handler(commands=["start"])
def default_test(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard1 = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
    url_button1 = types.InlineKeyboardButton(text="Перейти в Гугл", url="https://google.ru")
    keyboard.add(url_button)
    keyboard1.add(url_button1)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик, но другой.", reply_markup=keyboard1)
    pass

@bot.message_handler(commands=["apply"])
def handle_start_help(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    contact_button = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    keyboard.add(contact_button)
    bot.send_message(message.chat.id, "Предоставьте нам свой номер телефона - мы свяжемся с вами!", reply_markup=keyboard)
    pass

@bot.message_handler(content_types=["contact"])
def handle_start_help(message):
    #bot.send_message(31036763, message.contact.phone_number)
    msg = message.contact.first_name + " " + message.contact.last_name + " " + message.contact.phone_number
    bot.send_message(31036763, msg)
    bot.send_message(31036763, "Kaйф")
    msg =  "*" + message.contact.first_name + " " + message.contact.last_name + "*, пошёл ты в жопу!"
    bot.send_message(message.chat.id, msg, parse_mode="Markdown")
    pass

@bot.message_handler(regexp="b")
def handle_start_help(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Давай узнаем, кто тут хозяин", callback_data="Кто тут хозяин?")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку!", reply_markup=keyboard)
    pass

#@bot.message_handler(regexp="Жалоба")
#def handle_start_help(message):
#    msg = "*" + message.chat.first_name + " " + message.chat.last_name+ "*,я один, а вас много! У меня обед! Что у тебя не так?!"
#    bot.send_message(message.chat.id, msg, parse_mode="Markdown")
#    Z="Имя: " + message.chat.first_name + " " + message.chat.last_name
#    z1=True
#    while z1:
#        @bot.message_handler(content_types=["text"])
#        def handle_start_help(message1):
#            Z = Z + " Текст сообщения: " + message1.text
#            msg = "*" + message.chat.first_name + "*, телефон диктуй!"
#            bot.send_message(message.chat.id, msg, parse_mode="Markdown")
#            z2=True
#            while z2:
#                @bot.message_handler(content_types=["text"])
#                def handle_start_help(message2):
#                    Z = Z + " Телефон: " + message2.text
#                    msg = "*" + message.chat.first_name + "*, всё пошёл отсюда!"
#                    bot.send_message(message.chat.id, msg, parse_mode="Markdown")
#                    z1,z2=False
#                    pass
#            pass
#
#    bot.send_message(31036763, Z)
#    pass
#


@bot.message_handler(regexp="1")
def handle_start_help(message):
    Z=""
    Z="Имя: " + message.chat.first_name + " " + message.chat.last_name
    msg = "*" + message.chat.first_name + "*, задайте вопрос!"
    bot.send_message(message.chat.id, msg, parse_mode="Markdown")
    Z = "Имя: " + message.chat.first_name + " " + message.chat.last_name
    pass


@bot.message_handler(regexp="Кто тут хозяин?")
def handle_start_help(message):
    if message.chat.id == 31036763:
        bot.send_message(message.chat.id, "Вы!")
    if message.chat.id != 31036763:
        bot.send_message(message.chat.id, "ПОШЁЛ ВОН, КОЗЁЛ!")

    pass




if __name__ == '__main__':
    bot.polling(none_stop=True)
