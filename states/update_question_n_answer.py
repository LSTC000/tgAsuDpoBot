from aiogram.dispatcher.filters.state import StatesGroup, State


class UpdateQuestionAndAnswerStatesGroup(StatesGroup):
    process_update_question_n_answer_picker = State()
    update_question_n_answer_menu = State()
    enter_new_question = State()
    enter_new_answer = State()
    confirm_update_question_n_answer_menu = State()
