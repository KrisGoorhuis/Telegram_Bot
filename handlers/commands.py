import os
import requests
import time

token = "hidden"
with open("token.txt") as tokenFile:
    for line in tokenFile:
        key, _, token = line.partition("=")


def start(bot, update):
    chat_id = update.message.chat_id
    text = "Hello there, {}! I'm a bot. Tell me to /help you for a list of orders. Otherwise I'd be more than happy to listen and, perhaps, respond to anything you'd like to say.".format(update.message.from_user.first_name)
    bot.send_message(chat_id, text)
    update.message.reply_text("Test")
    
def help(bot, update):
    print("{} typed {}".format(update.message.chat.first_name, update.message.text))
    bot.send_message(chat_id=update.message.chat_id, text=("""
    Currently I know how to...
        /list_images
        /get <image name> to download an image.
            - To save an image, post it here with your preferred 
              title inside its caption. No extention needed.
        /sing !

        


    """))

def sing(bot, update, args):
    print("{} typed {}".format(update.message.chat.first_name, update.message.text))
    received = update.message.text
    argsString = " ".join(args)

    if (re.match(r"(t|T)wisted\s*(s|S)ister", argsString)):
        bot.send_message(chat_id=update.message.chat_id, text="Oh we're not gonna take it")
        time.sleep(4)
        bot.send_message(chat_id=update.message.chat_id, text="No, we ain't gonna take it!")
        time.sleep(4)
        bot.send_message(chat_id=update.message.chat_id, text="Oh we're not gonna take it... anymoooooooooore")

    else:
        bot.send_message(chat_id=update.message.chat_id, text="What should I sing? I know bits of Twisted Sister, and... nothing else at the moment. ")
    
def list_images(bot, update):
    print("{} typed {}".format(update.message.chat.first_name, update.message.text))
    images = os.listdir(r"C:/Users/Kris/Google Drive/Python Stuff/Images/")
    imageList = "\n"
    for image in images:
        imageList += "{}\n".format(image)
    print(imageList)
    bot.send_message(chat_id=update.message.chat_id, text="I found images with the names... {}".format(imageList))
    bot.send_message(chat_id=update.message.chat_id, text="To request an image, use \"/get (filename)\"")

def get(bot, update, args):
    print("{} typed {}".format(update.message.chat.first_name, update.message.text))
    if (len(args) == 0):
        bot.send_message(chat_id=update.message.chat_id, text="Which image did you want to get? use \"/list_images\" to see what's available.")
    else:
        imageFolder = r"C:/Users/Kris/Google Drive/Python Stuff/Images/"
        folderList = os.listdir(r"C:/Users/Kris/Google Drive/Python Stuff/Images/")
        requestedImage = "{}{}".format(imageFolder, args[0])

        if (args[0] in folderList):
            bot.send_message(chat_id=update.message.chat_id, text="Just a moment...")
            print("getting {}".format(requestedImage))
            photo = {'photo': open(requestedImage, 'rb')}
            status = requests.post(('https://api.telegram.org/bot{}/sendPhoto?chat_id={}').format(token, update.message.chat_id), files=photo)
            print("status:")
            print(status)
        else:
            bot.send_message(chat_id=update.message.chat_id, text="Looks like that image isn't in the (case sensitive) list.")
        
def save(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text="If you're trying to save an image, post it here with your preferred title inside its caption. No extention needed.")

def coffee(bot, update, args):
    print("{} typed {}".format(update.message.chat.first_name, update.message.text))
    
    if time.localtime().tm_hour < 8:
        bot.send_message(chat_id=update.message.chat_id, text="Good morning!")    
        time.sleep(1)

    bot.send_message(chat_id=update.message.chat_id, text="Starting a three minute timer.")
    time.sleep(60*3)
    bot.send_message(chat_id=update.message.chat_id, text="Coffee's done.")
