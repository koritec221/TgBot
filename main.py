import telebot
from telebot.types import Message
import random
import os
a = random.randint(0,1000)
bot = telebot.TeleBot('7574521663:AAH4uXeziO8q6AttO8wxnmz9nAGmSzQrcms')


@bot.message_handler(commands=['start'])
def start(message: Message):
    bot.reply_to(message, 'Привет!')


@bot.message_handler(commands=['random'])
def cmd_random(message:Message):
    if random.randint(0,1) == 0:
        bot.reply_to(message, 'Вам выпал орел!')
    else:
        bot.reply_to(message, 'Вам выпал решка!')


@bot.message_handler(commands=['name'])
def cmd_name(message:Message):
    bot.reply_to(message, 'Меня зовут Джек')


@bot.message_handler(commands=['randomiser'])
def cmd_randomiser(message:Message):
    bot.reply_to(message, a)


@bot.message_handler(commands=['task'])
def cmd_task(message:Message):
    with open('task.txt','a',encoding='utf-8') as file:
        file.write(message.text)
        bot.reply_to(message,'Задача добавлена') 


@bot.message_handler(commands=['read'])
def cmd_read(message:Message):
    with open('task.txt','r',encoding='utf-8') as file:
        bot.reply_to(message,file.read())


@bot.message_handler(commands=['mem'])
def cmd_mem(message:Message):
    pictures = os.listdir('meme')
    with open('meme/' +  random.choice (pictures),'rb') as file:
        bot.send_photo(message.chat.id , file)










bot.polling()
