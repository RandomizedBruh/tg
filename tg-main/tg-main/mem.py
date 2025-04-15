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
        "title":"5 бублей",
        "description": "Mem from pyat' bubles",
        "imgList":["rubels.png"],
        "source": "Gamebanana",
        "CreatedAt":"07.06.2024",
        "author":"Matr4ss or 5rubls team",
        "tags":["fnf", "mods"]
    },
    {
        "title":"DO YA WANT F###ing corn?",
        "description": "ITZ DVAE AND BMABI OOOHH",
        "imgList":["corn.png"],
        "source": "Gamebanana",
        "CreatedAt":"какоетотам.00.2021",
        "author":"moldyGH or dnb team",
        "tags":["fnf", "mods"]
    },
    {
        "title":"огарцы)))))0",
        "description": "огурчеки))",
        "imgList":["cucumberi.jpg"],
        "source": "магазинес двадцать четыри",
        "CreatedAt":"какоетотам.00.2025",
        "author":"THEREELLIMON",
        "tags":["random"]
    }

] 

tagList = set()
for mem in lib:
    for tag in mem["tags"]:
        tagList.add(tag)
print("Tags:", tagList)
    



TOKEN = "7683440220:AAHsKjlRCWdf6z1RKKwIaqUHYi6nFfiipzg"
bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'начать'])
def start_message(message):
    print(message)
    bot.send_message(message.chat.id, "перевет я зацикленный на одной и той же игре мембот - напиши чё нить, и я тоже напишу   #Tags")

@bot.message_handler(commands=["tags", "теги", "tag", "тег"])
def tags_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for tag in tagList:
        btn= types.KeyboardButton(tag)
        markup.add(btn)
    bot.send_message(message.chat.id, "тегнем щас бум", reply_markup=markup)

@bot.message_handler(commands=['button',"b"])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = types.KeyboardButton("кнопка1")
    b2 = types.KeyboardButton("кнопка2")
    markup.add(b1,b2)
    bot.send_message(message.chat.id, "кнопочккки",reply_markup=markup)

@bot.message_handler(content_types =['text'])
def message(message:types.Message):
    chat_id = message.chat.id
    text = message.text.lower()
    isFound = False



    for mem in lib:
        title:str = mem["title"]
        description:str=mem["description"] 
        tags:list =mem["tags"]
        author:str = mem["author"]



        if text in title.lower() or text in mem["description"].lower() or text in mem["tags"] or text in author.lower():
            isFound = True
            bot.send_message(message.chat.id, f"Meme's name: {title}\n\nDescription: {description}")
            for photo in mem["imgList"]:
                bot.send_photo(chat_id, open("./img/"+photo, "rb"))

    if not isFound:
        bot.send_message(chat_id,"не получилось, не фортануло, нету тут такого")
            

@bot.message_handler(content_types=["sticker"])
def send_sticker_id(message):
    print(message.sticker.file_id)
    bot.send_message(message.chat.id, f"ID sticker: {message.sticker.file_id}")


print("превет")
bot.infinity_polling()
