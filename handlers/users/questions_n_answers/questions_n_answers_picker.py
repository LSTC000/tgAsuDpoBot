from loader import dp, bot

from data.redis import LAST_IKB_REDIS_KEY

from database import get_answer

from functions import clear_last_ikb, get_questions_cache

from keyboards import question_n_answer_report_ikb

from pickers import QuestionsAndAnswersPicker

from states import QuestionsAndAnswersPickerStatesGroup

from utils import create_question_n_answer_report

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(state=QuestionsAndAnswersPickerStatesGroup.questions_n_answers_picker)
async def questions_n_answers_picker(callback: types.CallbackQuery, state: FSMContext) -> None:
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
            # Call questions and answers picker inline menu.
            msg = await bot.send_message(
                chat_id=user_id,
                text=create_question_n_answer_report(question=question, answer=await get_answer(question_id)),
                reply_markup=question_n_answer_report_ikb()
            )
            # Remember id of the last inline keyboard.
            data[LAST_IKB_REDIS_KEY] = msg.message_id

        # Set question_n_answer_report state.
        await QuestionsAndAnswersPickerStatesGroup.question_n_answer_report.set()
