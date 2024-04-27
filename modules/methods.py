from configparser import ConfigParser
from modules.random import GemRandom
from telebot import TeleBot
from modules.markups import Markups

class BotTweaker:
    def __init__(self, bot: TeleBot, config: ConfigParser):
        self.bot = bot
        self.markups = Markups(config)
        self.config = config

    def start(self, message):
        self.bot.send_message(message.from_user.id, self.config['Messages']['start'], reply_markup=self.markups.get_markup(0))

    def generate_password(self, message):
        self.bot.send_message(message.from_user.id, self.config['Messages']['result'])
        self.bot.send_message(message.from_user.id, GemRandom.gen_rand_str(16, True), reply_markup=self.markups.get_markup(0))

    def generate_username(self, message):
        self.bot.send_message(message.from_user.id, self.config['Messages']['result'])
        self.bot.send_message(message.from_user.id, GemRandom.gen_rand_str(8, False), reply_markup=self.markups.get_markup(0))
    
    def undefined(self, message):
        self.bot.send_message(message.from_user.id, self.config['Messages']['undefined'], reply_markup=self.markups.get_markup(0))
