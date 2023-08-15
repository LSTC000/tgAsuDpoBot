__all__ = ['register_users_main_menu']


from .change_user_alert import change_user_alert

from aiogram import Dispatcher


def register_users_main_menu(dp: Dispatcher):
    dp.register_callback_query_handler(change_user_alert)
