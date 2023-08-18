from loader import dp, bot

from data.messages import ERROR_ENTER_QUESTION_MESSAGE

from data.redis import QUESTION_REDIS_KEY

from functions import clear_last_ikb, call_update_question_n_answer_menu_ikb

from utils import Validator

from states import UpdateQuestionAndAnswerStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=UpdateQuestionAndAnswerStatesGroup.enter_new_question)
async def enter_new_question(message: types.Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    text = message.text

    # Clear last inline keyboard.
    await clear_last_ikb(user_id=user_id, state=state)
    # Check new question on valid.
    if Validator().question_validation(text):
        async with state.proxy() as data:
            data[QUESTION_REDIS_KEY] = text
    else:
        await bot.send_message(chat_id=user_id, text=ERROR_ENTER_QUESTION_MESSAGE)

    # Call update question and answer inline menu.
    await call_update_question_n_answer_menu_ikb(user_id=user_id, state=state)
    # Set add_question_n_answer_menu state.
    await UpdateQuestionAndAnswerStatesGroup.update_question_n_answer_menu.set()
