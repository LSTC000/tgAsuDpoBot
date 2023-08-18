from aiogram.dispatcher.filters.state import StatesGroup, State


class QuestionsAndAnswersPickerStatesGroup(StatesGroup):
    questions_n_answers_picker = State()
    question_n_answer_report = State()
