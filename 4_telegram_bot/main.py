from telegram.ext import Updater, CommandHandler
import requests
import re

import os # for env var
from dotenv import load_dotenv
load_dotenv() # to load .env to environment variables, so we can use os.environ


# This function fetches the dog public API to get a dog url (image, gif, etc)
def get_url():
    # accessing the API and getting json data
    URL = 'https://random.dog/woof.json'
    contents = requests.get(URL).json()
    image_url = contents['url'] # getting the url key from the json above
    return image_url

def get_media_or_photo_url():
    allowed_extension = ['jpg','jpeg','png', 'gif']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url, file_extension

def get_doggo(bot, update):
    # url = get_image_url()
    url, file_extension = get_media_or_photo_url()
    chat_id = update.message.chat_id
    
    if file_extension == 'gif': # https://python-telegram-bot.readthedocs.io/en/stable/telegram.bot.html?highlight=send_photo#telegram.Bot.send_animation
        bot.send_animation(chat_id=chat_id, animation=url)
    else: # https://python-telegram-bot.readthedocs.io/en/stable/telegram.bot.html?highlight=send_photo#telegram.Bot.send_photo
        bot.send_photo(chat_id=chat_id, photo=url)


#######################
####### MAIN ##########
#######################

def main():
    TOKEN = os.environ['DOG_API_TOKEN']
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('doggo', get_doggo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

