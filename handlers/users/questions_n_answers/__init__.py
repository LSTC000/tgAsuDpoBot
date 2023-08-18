__all__ = ['register_users_questions_n_answers']


from .questions_n_answers import questions_n_answers
from .questions_n_answers_picker import questions_n_answers_picker

from aiogram import Dispatcher


def register_users_questions_n_answers(dp: Dispatcher):
    dp.register_callback_query_handler(questions_n_answers)
    dp.register_callback_query_handler(questions_n_answers_picker)
