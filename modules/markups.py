from telebot import types
from configparser import ConfigParser

class Markups:
    def __init__(self, config: ConfigParser) -> None:
        main_btns = [
            types.KeyboardButton(config['Keyboards']['gen_pass']),
            types.KeyboardButton(config['Keyboards']['gen_user'])
           ]
        self.keyboards = []
        self.inline_keyboards = []

        main = types.ReplyKeyboardMarkup(True)
        for b in main_btns:
            main.add(b)
        
        self.keyboards.append(main)

    def get_markup(self, id: int):
        return self.keyboards[id]
    
    def get_inline_markup(self, id: int):
        return self.inline_keyboards[id]
