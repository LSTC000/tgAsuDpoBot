from aiogram.dispatcher.filters.state import StatesGroup, State


class DeleteQuestionAndAnswerStatesGroup(StatesGroup):
    process_delete_question_n_answer_picker = State()
    confirm_delete_question_n_answer_menu = State()
