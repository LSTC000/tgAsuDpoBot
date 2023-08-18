from loader import dp

from data.callbacks import SAVE_ADD_QUESTION_N_ANSWER_CALLBACK_DATA

from data.messages import ERROR_ENTER_QUESTION_MESSAGE, ERROR_ENTER_ANSWER_MESSAGE

from data.redis import QUESTION_REDIS_KEY, ANSWER_REDIS_KEY

from functions import clear_last_ikb, call_confirm_add_question_n_answer_menu_ikb

from states import AddQuestionAndAnswerStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(
    lambda c: c.data == SAVE_ADD_QUESTION_N_ANSWER_CALLBACK_DATA,
    state=AddQuestionAndAnswerStatesGroup.add_question_n_answer_menu
)
async def save_add_question_n_answer(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    async with state.proxy() as data:
        question = data[QUESTION_REDIS_KEY] if QUESTION_REDIS_KEY in data else None
        answer = data[ANSWER_REDIS_KEY] if ANSWER_REDIS_KEY in data else None

    if question is None:
        await callback.answer(text=ERROR_ENTER_QUESTION_MESSAGE, show_alert=True)
    elif answer is None:
        await callback.answer(text=ERROR_ENTER_ANSWER_MESSAGE, show_alert=True)
    else:
        # Clear last inline keyboard.
        await clear_last_ikb(user_id=user_id, state=state)
        # Call confirm add question and answer inline menu.
        await call_confirm_add_question_n_answer_menu_ikb(user_id=user_id, state=state)
        # Set confirm_add_question_n_answer_menu state.
        await AddQuestionAndAnswerStatesGroup.confirm_add_question_n_answer_menu.set()
