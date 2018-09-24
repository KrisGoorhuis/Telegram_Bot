
import re
import requests
# import urllib
import json
import os

token = "hidden"
with open("token.txt") as tokenFile:
    for line in tokenFile:
        key, _, token = line.partition("=")

def photoHandler(bot, update):
    # Sending a photo to the bot results in it being stored by the Telegram folks for an hour. We grab it from them and save it for ourselves.
    our_file_id = update.message.photo[0].file_id
    getFile_info_raw_response = requests.get("https://api.telegram.org/bot{}/getFile?file_id={}".format(token, our_file_id))
    our_file_path = getFile_info_raw_response.json()["result"]["file_path"]
    download_link = "https://api.telegram.org/file/bot{}/{}".format(token, our_file_path)

    if update.message.caption == None:
        bot.send_message(chat_id=update.message.chat_id, text="You didn't provide a caption! What would you like to call this photo?")
        return

    print((re.search(r"^(.*?)\..*", update.message.caption)))
    extention = (re.search(r"(\..+)", our_file_path)).group(0) # Grabs the extention of the uploaded file. So we can...
    title = (re.search(r"^(.*?)\..*", update.message.caption)).group(0) # Drop extentions from user input. This way it doesn't matter if they provide one. They can still make it wonky, though.
    full_title = title + extention
    print(title)
    print(extention)

    existingImages = os.listdir(r"C:/Users/Kris/Google Drive/Python Stuff/Images/")
    imageList = []
    for image in existingImages:
        imageList.append(image)
    
    if full_title in imageList:
        print("Photo {} already exists".format(full_title))
        bot.send_message(chat_id=update.message.chat_id, text="An image with that name already exists! Please choose another.")
    else:
        try:
            print("Saving photo as {}{}".format(update.message.caption, extention))
            photo = open(r"C:/Users/Kris/Google Drive/Python Stuff/Images/{}".format(full_title), "wb")
            photo.write(requests.get(download_link).content)
            photo.close()
            bot.send_message(chat_id=update.message.chat_id, text="Image saved as \"{}\"".format(full_title))
        except Exception as problemo:
            print("Some kind of exception!")
            print(problemo)
            bot.send_message(chat_id=update.message.chat_id, text="Image wasn't saved. Either I'm broken or the caption wasn't a valid file name.")



def chatHandler(bot, update):
    received = update.message.text
    chat_id = update.message.chat_id
    print("{} said '{}'".format(update.message.chat.first_name, received))

    #General chat matches:

    if (re.match(r"^help$", received)):
        bot.send_message(chat_id=chat_id, text="Did you mean '/help'?")

        # Hello - any known variation
    if (re.match(r"\w\wllo", received) and len(received) <= 15):
        print(received)
        bot.send_message(chat_id=chat_id, text="Hello {}!".format(update.message.from_user.first_name))
        # Thank you
    if (re.match(r"\whank you", received)):
        bot.send_message(chat_id=chat_id, text="My pleasure, as always.")

    # Faces:
    if (re.match(r"^o.o", received)):
        bot.send_message(chat_id=chat_id, text="o.o")
        time.sleep(2)
        bot.send_message(chat_id=chat_id, text="O.O")

    if (re.match(r"^O.O", received)):
        bot.send_message(chat_id=chat_id, text="...")
        bot.send_message(chat_id=chat_id, text="Hello snail.")

    if (re.match(r"^^n.n|^\^_+\^", received)):
        bot.send_message(chat_id=chat_id, text="o.o")

    if (re.match(r"^@.@", received)):
        bot.send_message(chat_id=chat_id, text="*patpatpat*")