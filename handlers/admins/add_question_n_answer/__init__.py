__all__ = ['register_admins_add_question_n_answer']


from .alert_for_users import alert_for_users
from .enter_alert_for_users import enter_alert_for_users
from .confirm_alert_for_users import confirm_alert_for_users

from aiogram import Dispatcher


def register_admins_add_question_n_answer(dp: Dispatcher):
    dp.register_callback_query_handler(alert_for_users)
    dp.register_message_handler(enter_alert_for_users)
    dp.register_callback_query_handler(confirm_alert_for_users)
