from loader import dp, bot

from data.callbacks import ADD_ANSWER_CALLBACK_DATA

from data.messages import ENTER_ANSWER_MESSAGE

from functions import clear_last_ikb

from states import AddQuestionAndAnswerStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(
    lambda c: c.data == ADD_ANSWER_CALLBACK_DATA,
    state=AddQuestionAndAnswerStatesGroup.add_question_n_answer_menu
)
async def add_answer(callback: types.CallbackQuery, state: FSMContext) -> None:
    # Clear last inline keyboard.
    await clear_last_ikb(user_id=callback.from_user.id, state=state)
    # Enter answer.
    await bot.send_message(chat_id=callback.from_user.id, text=ENTER_ANSWER_MESSAGE)
    # Set enter_answer state.
    await AddQuestionAndAnswerStatesGroup.enter_answer.set()
