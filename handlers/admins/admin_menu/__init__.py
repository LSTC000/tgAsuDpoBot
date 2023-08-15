__all__ = ['register_admin_menu']


from .alert_for_users import enter_alert_for_users, alert_for_users, confirm_alert_for_users

from aiogram import Dispatcher


def register_admin_menu(dp: Dispatcher):
    dp.register_callback_query_handler(enter_alert_for_users)
    dp.register_message_handler(alert_for_users)
    dp.register_callback_query_handler(confirm_alert_for_users)
