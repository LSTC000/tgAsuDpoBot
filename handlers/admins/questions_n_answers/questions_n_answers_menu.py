from loader import dp

from data.callbacks import QUESTIONS_N_ANSWERS_CALLBACK_DATA

from functions import clear_last_ikb, call_questions_n_answers_menu_ikb

from states import AdminMenuStatesGroup, QuestionsAndAnswersMenuStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(lambda c: c.data == QUESTIONS_N_ANSWERS_CALLBACK_DATA, state=AdminMenuStatesGroup.admin_menu)
async def questions_n_answers_menu(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    # Clear last inline keyboard.
    await clear_last_ikb(user_id=user_id, state=state)
    # Call questions and answers menu.
    await call_questions_n_answers_menu_ikb(user_id=user_id, state=state)
    # Set questions_n_answers_menu state.
    await QuestionsAndAnswersMenuStatesGroup.questions_n_answers_menu.set()
