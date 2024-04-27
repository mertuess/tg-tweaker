from telebot import TeleBot
import configparser
from modules.methods import BotTweaker

config = configparser.ConfigParser()
config.read("config.ini", encoding='utf-8')

bot = TeleBot(config['Bot']['token'])
tweaker = BotTweaker(bot, config)

# Handliers
@bot.message_handler(commands = ['start'])
def start(message):
    tweaker.start(message)

@bot.message_handler(commands = ['gen_pass'])
def generate_password(message):
    tweaker.generate_password(message)

@bot.message_handler(commands = ['gen_user'])
def generate_username(message):
    tweaker.generate_username(message)

@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == config['Keyboards']['gen_pass']:
        tweaker.generate_password(message)
    elif message.text == config['Keyboards']['gen_user']:
        tweaker.generate_username(message)
    else:
        tweaker.undefined(message)

bot.polling(non_stop=True, interval=0)
