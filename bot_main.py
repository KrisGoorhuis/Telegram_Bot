import telegram
# import time
import re
import os
# import requests
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
# import logging

token = "hidden"
with open("token.txt") as tokenFile:
    for line in tokenFile:
        key, _, token = line.partition("=")
    
updater = Updater(token=token)
dispatcher = updater.dispatcher
bot = telegram.Bot(token=token)
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)



import handlers.message_handlers
dispatcher.add_handler(MessageHandler(Filters.text, handlers.message_handlers.chatHandler))

dispatcher.add_handler(MessageHandler(Filters.photo, handlers.message_handlers.photoHandler))

import handlers.commands
dispatcher.add_handler(CommandHandler("start", handlers.commands.start))
dispatcher.add_handler(CommandHandler("help", handlers.commands.help))
dispatcher.add_handler(CommandHandler("sing", handlers.commands.sing, pass_args=True))
dispatcher.add_handler(CommandHandler("list_images", handlers.commands.list_images))
dispatcher.add_handler(CommandHandler("get", handlers.commands.get, pass_args=True))
dispatcher.add_handler(CommandHandler("save", handlers.commands.save, pass_args=True))
dispatcher.add_handler(CommandHandler("coffee", handlers.commands.coffee, pass_args=True))


print(bot.get_me())
updater.start_polling()
updater.idle()

