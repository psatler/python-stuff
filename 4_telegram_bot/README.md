> A bot which sends random images or gifs of dogs

Tulipa bot sends random images or gifs as a response of a command. 

Using the public API [https://random.dog/](https://random.dog/)

Access the bot via the following url (if using Web/Desktop Telegram): [https://telegram.me/tulipa_bot](https://telegram.me/tulipa_bot) or via @tulipa_bot

# Commands
Currently, there is only one command. 
```
/doggo - typing it and confirming sends random images or gifs of dogs
```

# How to run locally
Install dependencies

```
pip3 install python-telegram-bot
pip3 install python-dotenv
pip3 install requests
```
Run the `main.py` file
```
python3 main.py
```

# Deploying to Heroku
TL;DR:
- Add a _requirements.txt_ with the dependencies needed
- Add a _Procfile_ with the command used to run the Python script (your main executable).
- I also added a _runtime.txt_ with the version I used
- Deployed to Heroku using its CLI, using the following commands: 
    ```
    heroku login
    heroku create
    git push heroku master
    heroku ps:scale worker=1
    heroku open (this probably will show an error)
    heroku logs --tail (to see the logs)
    ```
For a more detailed explanation of the process of deploying to [heroku](https://devcenter.heroku.com/categories/reference), check this [repository](https://github.com/michaelkrukov/heroku-python-script).
# Dependencies

- python-telegram-bot: [https://python-telegram-bot.readthedocs.io/en/stable/](https://python-telegram-bot.readthedocs.io/en/stable/)
- python-dotenv: to load `.env` variables
- requests: to perform http requests

# Useful links
- [Core API Docs of Telegram](https://core.telegram.org/bots/api#sendmessage): It has the methods and its parameters and description

Links below are not only related to Python
- [Bot with Nodejs deployed to Now](https://scotch.io/tutorials/how-to-build-a-telegram-bot-using-nodejs-and-now)
- [Marco Polo Bot with Nodejs](https://www.sohamkamani.com/blog/2016/09/21/making-a-telegram-bot/)
- [Serverless Python Telegram bot](https://medium.freecodecamp.org/how-to-build-a-server-less-telegram-bot-227f842f4706)
- [Webhook using self-signed certificate and Flask (with python-telegram-bot library)](https://gist.github.com/leandrotoledo/4e9362acdc5db33ae16c)
- [Echo bot with Python - Both parts 1 and 2](https://www.reddit.com/r/Python/comments/5hctvj/tutorials_building_telegram_bots_using_python/)