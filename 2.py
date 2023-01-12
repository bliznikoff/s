

# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message): # Название функции не играет никакой роли
#     bot.send_message(message.chat.id, message.text)

# if __name__ == '__Bot__':
#      bot.infinity_polling()    

# def rand(update, context):
#     context.bot.send_message(update.effective_chat.id, f'{rd(1, 100)}')


# start_handler = CommandHandler('start', start)
# random_handler = CommandHandler('random', rand)


# dispatcher.add_handler(start_handler)
# dispatcher.add_handler(random_handler)

# def func(update, context):
#     context.bot.send_message(update.effective_chat.id,"Я не знаю таких команд")

# start_handler = CommandHandler('start', start)
# random_handler = CommandHandler('random', rand)
# message_handler = MessageHandler(Filters.voice, func)

# dispatcher.add_handler(start_handler)
# dispatcher.add_handler(random_handler)
# dispatcher.add_handler(message_handler)
# tart_handler = CommandHandler('start', start)
# random_handler = CommandHandler('random', rand)
# message_handler = MessageHandler(Filters.text, func)

# dispatcher.add_handler(start_handler)
# dispatcher.add_handler(random_handler)
# dispatcher.add_handler(message_handler)