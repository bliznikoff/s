from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint as rd

TOKEN = '5821155134:AAEw6MFVu5TX2LRI3kWL2x7nRh5Ug413WKw'
bot = Bot(token='5821155134:AAEw6MFVu5TX2LRI3kWL2x7nRh5Ug413WKw')
updater = Updater(token='5821155134:AAEw6MFVu5TX2LRI3kWL2x7nRh5Ug413WKw')
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Hello')

def abv_del(update, context):
    text = update.message.text.split()
    list = []
    for i in text:
        if 'абв' not in i:
            list.append(i)
    context.bot.send_message(update.effective_chat.id, ''.join(list))        

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
del_handler = MessageHandler(Filters.text, abv_del)
dispatcher.add_handler(del_handler)

updater.start_polling()
updater.idle()

