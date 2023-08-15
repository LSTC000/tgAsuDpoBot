__all__ = ['register_users_cancels']


from .cancel_to_main_menu import cancel_to_main_menu

from aiogram import Dispatcher


def register_users_cancels(dp: Dispatcher):
    dp.register_callback_query_handler(cancel_to_main_menu)
