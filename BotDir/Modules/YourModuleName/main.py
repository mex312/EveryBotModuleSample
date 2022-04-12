import telebot
from every_bot.types import Module, Core


class YourModuleName(Module):
    name = 'YourModuleName'
    bot: telebot.TeleBot

    def __init__(self, core: Core):
        super().__init__(core)

        self.bot = self.core.bot

        @self.bot.message_handler(commands=['hello'])
        def hello(message: telebot.types.Message):
            core.delete_message(message)
            self.bot.send_message(chat_id=message.chat.id, text="Hello!")

    """Bot's core will call it when user type /help"""
    """It will merge like '[yourReturn] from [YourModuleName]' """
    def help(self):
        return '/hello'


def get_module(core):
    return YourModuleName(core)
