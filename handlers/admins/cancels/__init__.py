__all__ = ['register_admins_cancels']


from .cancel_to_admin_menu import cancel_to_admin_menu
from .cancel_to_questions_n_answers_menu import cancel_to_questions_n_answers_menu

from aiogram import Dispatcher


def register_admins_cancels(dp: Dispatcher):
    dp.register_callback_query_handler(cancel_to_admin_menu)
    dp.register_callback_query_handler(cancel_to_questions_n_answers_menu)
