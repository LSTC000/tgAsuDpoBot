__all__ = ['register_admins_questions_n_answers']


# QUESTIONS AND ANSWERS.
from .questions_n_answers_menu import questions_n_answers_menu
# ADD QUESTION AND ANSWER.
from .add_question_n_answer import add_question_n_answer_menu
from .add_question_n_answer import add_question
from .add_question_n_answer import add_answer
from .add_question_n_answer import enter_question
from .add_question_n_answer import enter_answer
from .add_question_n_answer import save_add_question_n_answer
from .add_question_n_answer import confirm_add_question_n_answer_menu

from aiogram import Dispatcher


def register_admins_questions_n_answers(dp: Dispatcher):
    dp.register_callback_query_handler(questions_n_answers_menu)
    dp.register_callback_query_handler(add_question_n_answer_menu)
    dp.register_callback_query_handler(add_question)
    dp.register_callback_query_handler(add_answer)
    dp.register_message_handler(enter_question)
    dp.register_message_handler(enter_answer)
    dp.register_callback_query_handler(save_add_question_n_answer)
    dp.register_callback_query_handler(confirm_add_question_n_answer_menu)
