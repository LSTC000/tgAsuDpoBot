from loader import dp, bot

from data.messages import ERROR_ENTER_ANSWER_MESSAGE

from data.redis import ANSWER_REDIS_KEY

from functions import clear_last_ikb, call_add_question_n_answer_menu_ikb

from utils import Validator

from states import AddQuestionAndAnswerStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=AddQuestionAndAnswerStatesGroup.enter_answer)
async def enter_answer(message: types.Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    text = message.text

    # Clear last inline keyboard.
    await clear_last_ikb(user_id=user_id, state=state)
    # Check answer on valid.
    if Validator().answer_validation(text):
        async with state.proxy() as data:
            data[ANSWER_REDIS_KEY] = text
    else:
        await bot.send_message(chat_id=user_id, text=ERROR_ENTER_ANSWER_MESSAGE)

    # Call add question and answer inline menu.
    await call_add_question_n_answer_menu_ikb(user_id=user_id, state=state)
    # Set add_question_n_answer_menu state.
    await AddQuestionAndAnswerStatesGroup.add_question_n_answer_menu.set()
