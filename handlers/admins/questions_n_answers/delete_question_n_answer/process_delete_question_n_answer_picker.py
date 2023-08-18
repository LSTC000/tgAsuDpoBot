from loader import dp

from data.redis import QUESTION_REDIS_KEY, QUESTION_ID_REDIS_KEY

from functions import clear_last_ikb, get_questions_cache, call_confirm_delete_question_n_answer_menu_ikb

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
        # Clear last inline keyboard.
        await clear_last_ikb(user_id=user_id, state=state)

        questions = await get_questions_cache()
        question_id = int(question_id)
        question = questions[question_id]

        async with state.proxy() as data:
            data[QUESTION_REDIS_KEY] = question
            data[QUESTION_ID_REDIS_KEY] = question_id

        # Call questions and answers picker inline menu.
        await call_confirm_delete_question_n_answer_menu_ikb(user_id=user_id, state=state)
        # Set question_n_answer_report state.
        await DeleteQuestionAndAnswerStatesGroup.confirm_delete_question_n_answer_menu.set()
