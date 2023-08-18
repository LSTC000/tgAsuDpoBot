from loader import dp

from data.callbacks import ADD_QUESTION_N_ANSWER_CALLBACK_DATA

from functions import clear_last_ikb, call_add_question_n_answer_menu_ikb

from states import QuestionsAndAnswersMenuStatesGroup, AddQuestionAndAnswerStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(
    lambda c: c.data == ADD_QUESTION_N_ANSWER_CALLBACK_DATA,
    state=QuestionsAndAnswersMenuStatesGroup.questions_n_answers_menu
)
async def add_question_n_answer_menu(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    # Clear last inline keyboard.
    await clear_last_ikb(user_id=user_id, state=state)
    # Call add question and answer inline menu.
    await call_add_question_n_answer_menu_ikb(user_id=user_id, state=state)
    # Set add_question_n_answer_menu state.
    await AddQuestionAndAnswerStatesGroup.add_question_n_answer_menu.set()
