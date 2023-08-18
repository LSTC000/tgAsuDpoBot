from aiogram.dispatcher.filters.state import StatesGroup, State


class AddQuestionAndAnswerStatesGroup(StatesGroup):
    add_question_n_answer_menu = State()
    enter_question = State()
    enter_answer = State()
    confirm_add_question_n_answer_menu = State()
