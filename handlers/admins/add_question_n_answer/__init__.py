__all__ = ['register_admins_add_question_n_answer']


from .add_question_n_answer_menu import add_question_n_answer_menu
from .add_question import add_question
from .add_answer import add_answer
from .enter_question import enter_question
from .enter_answer import enter_answer
from .save_add_question_n_answer import save_add_question_n_answer
from .confirm_add_question_n_answer_menu import confirm_add_question_n_answer_menu

from aiogram import Dispatcher


def register_admins_add_question_n_answer(dp: Dispatcher):
    dp.register_callback_query_handler(add_question_n_answer_menu)
    dp.register_callback_query_handler(add_question)
    dp.register_callback_query_handler(add_answer)
    dp.register_message_handler(enter_question)
    dp.register_message_handler(enter_answer)
    dp.register_callback_query_handler(save_add_question_n_answer)
    dp.register_callback_query_handler(confirm_add_question_n_answer_menu)
