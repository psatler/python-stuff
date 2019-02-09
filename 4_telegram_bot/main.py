from telegram.ext import Updater, CommandHandler
import requests
import re

import os # for env var
from dotenv import load_dotenv
load_dotenv() # to load .env to environment variables, so we can use os.environ


class Bot_Handler:
    def __init__(self, token):
        self.token = token
        self.telegram_api_url = "https://api.telegram.org/bot{}/".format(token)
        self.dog_api_url = 'https://random.dog/woof.json'

    # This method fetches the dog public API to get a dog url (image, gif, etc)
    def get_url(self):
        contents = requests.get(self.dog_api_url).json() # accessing the API and getting json data
        image_url = contents['url'] # getting the url key from the json above
        return image_url

    def get_media_or_photo_url(self):
        allowed_extension = ['jpg','jpeg','png', 'gif']
        file_extension = ''
        while file_extension not in allowed_extension:
            url = self.get_url() # using above method
            file_extension = re.search("([^.]*)$",url).group(1).lower()
        return url, file_extension

    def get_doggo(self, bot, update):
        url, file_extension = self.get_media_or_photo_url()
        chat_id = update.message.chat_id
        print('chat_id', chat_id)
        
        if file_extension == 'gif': # https://python-telegram-bot.readthedocs.io/en/stable/telegram.bot.html?highlight=send_photo#telegram.Bot.send_animation
            bot.send_animation(chat_id=chat_id, animation=url)
        else: # https://python-telegram-bot.readthedocs.io/en/stable/telegram.bot.html?highlight=send_photo#telegram.Bot.send_photo
            bot.send_photo(chat_id=chat_id, photo=url)


#######################
####### MAIN ##########
#######################

def main():
    TOKEN = os.environ['DOG_API_TOKEN']
    bot = Bot_Handler(TOKEN)
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('doggo', bot.get_doggo))
    updater.start_polling(timeout=100) 
    updater.idle()

if __name__ == '__main__':
    main()

