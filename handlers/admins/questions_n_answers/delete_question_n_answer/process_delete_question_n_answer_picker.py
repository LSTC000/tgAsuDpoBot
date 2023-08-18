from loader import dp

from data.redis import QUESTION_ID_REDIS_KEY

from functions import clear_last_ikb, call_confirm_delete_question_n_answer_menu_ikb

from pickers import QuestionsAndAnswersPicker

from states import DeleteQuestionAndAnswerStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(state=DeleteQuestionAndAnswerStatesGroup.process_delete_question_n_answer_picker)
async def process_delete_question_n_answer_picker(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    choice, question_id = await QuestionsAndAnswersPicker().process_selection(
        callback=callback,
        callback_data=callback.data,
        state=state
    )

    if choice:
        async with state.proxy() as data:
            data[QUESTION_ID_REDIS_KEY] = question_id

        # Clear last inline keyboard.
        await clear_last_ikb(user_id=user_id, state=state)
        # Call confirm delete question and answer inline menu.
        await call_confirm_delete_question_n_answer_menu_ikb(user_id=user_id, state=state)
        # Set question_n_answer_report state.
        await DeleteQuestionAndAnswerStatesGroup.confirm_delete_question_n_answer_menu.set()
