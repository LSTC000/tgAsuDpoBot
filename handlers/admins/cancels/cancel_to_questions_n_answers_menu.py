from loader import dp

from data.callbacks import CANCEL_TO_QUESTIONS_N_ANSWERS_MENU_CALLBACK_DATA

from functions import clear_last_ikb, clear_redis_data, call_questions_n_answers_menu_ikb

from states import (
    QuestionsAndAnswersMenuStatesGroup,
    AddQuestionAndAnswerStatesGroup,
    DeleteQuestionAndAnswerStatesGroup,
)

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(
    lambda c: c.data == CANCEL_TO_QUESTIONS_N_ANSWERS_MENU_CALLBACK_DATA,
    state=[
        AddQuestionAndAnswerStatesGroup.add_question_n_answer_menu,
        DeleteQuestionAndAnswerStatesGroup.process_delete_question_n_answer_picker,
    ]
)
async def cancel_to_questions_n_answers_menu(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    # Clear redis data.
    await clear_redis_data(state=state)
    # Clear last inline keyboard.
    await clear_last_ikb(user_id=user_id, state=state)
    # Call questions and answers inline menu.
    await call_questions_n_answers_menu_ikb(user_id=user_id, state=state)
    # Set questions_n_answers_menu state.
    await QuestionsAndAnswersMenuStatesGroup.questions_n_answers_menu.set()
