__all__ = ['register_users_cancels']


from .cancel_to_main_menu import cancel_to_main_menu
from .cancel_to_questions_n_answers import cancel_to_questions_n_answers

from aiogram import Dispatcher


def register_users_cancels(dp: Dispatcher):
    dp.register_callback_query_handler(cancel_to_main_menu)
    dp.register_callback_query_handler(cancel_to_questions_n_answers)
