import logging

from aiogram import Dispatcher, executor

from loader import dp
from handlers.main_handlers import get_start, button_pressed


logging.basicConfig(level=logging.INFO)


def register_handlers(dp : Dispatcher):
    dp.register_message_handler(get_start, commands=['start', 'help'])
    dp.register_callback_query_handler(button_pressed)
    
register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True)