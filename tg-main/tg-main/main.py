import telebot
from telebot import types
from random import choice

sticker_list=[
    "CAACAgIAAxkBAAO8Z-uVe3gLsprTZm2ZLRBIeTH_KZEAAnk4AALdQrBJFtfAcciPNXg2BA",
    "CAACAgIAAxkBAAPDZ-uWaDz45YP-bUBKErGdO_m460kAAnA3AAKaD7FJd_9fNs8kZ9Y2BA",
    "CAACAgIAAxkBAAPFZ-uWdXfyI5n1m3ZLb-IpkiXnOdAAAko-AAKMgqlJBG7I6xsr6r42BA",
    "CAACAgIAAxkBAAPGZ-uWdlrVl9cxcjjri0IJTBBp6BwAAi0zAAKK07FJSjEyh8awYk82BA",
    "CAACAgIAAxkBAAPHZ-uWg9Grh0tkygN9RH50jcBPVSQAAgU4AAKde7BJJ2JphMMLeqU2BA"
]




lib = [
    {
        "title":"sharite za rubliki?",
        "description": "Mem from pyat' bubles",
        "imgList":["rubels.png"],
        "source": "funkysite",
        "CreatedAt":"07.06.2024",
        "author":"Matr4ss or 5rubls team"
    }
] 





TOKEN = "7683440220:AAFLJ74Ka-M4S_DcAUCL00NtCDAMFBNKAvU"
bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'st'])
def start_message(message):
    print(message)
    bot.send_message(message.chat.id, "шариш за пят рублес?")
    bot.send_photo(message.chat.id,  open("./img/rybles.png", "rb"))



@bot.message_handler(commands=['button',"b"])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = types.KeyboardButton("кнопка1")
    b2 = types.KeyboardButton("кнопка2")
    markup.add(b1,b2)
    bot.send_message(message.chat.id, "кнопочккки",reply_markup=markup)

@bot.message_handler(content_types =['text'])
def message(message):
    if message.text=="кнопка1":
       bot.send_message(message.chat.id,"эпикФейл")
       bot.send_sticker(message.chat.id, choice(sticker_list))
    elif message.text=="кнопка2":
        bot.send_message(message.chat.id,"Эпигандо")

@bot.message_handler(content_types=["sticker"])
def send_sticker_id(message):
    print(message.sticker.file_id)
    bot.send_message(message.chat.id, f"ID sticker: {message.sticker.file_id}")


print("превет")
bot.infinity_polling()
