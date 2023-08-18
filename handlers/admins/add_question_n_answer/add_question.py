from loader import dp, bot

from data.callbacks import ADD_QUESTION_CALLBACK_DATA

from data.messages import ENTER_QUESTION_MESSAGE

from functions import clear_last_ikb

from states import AddQuestionAndAnswerStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(
    lambda c: c.data == ADD_QUESTION_CALLBACK_DATA,
    state=AddQuestionAndAnswerStatesGroup.add_question_n_answer_menu
)
async def add_question(callback: types.CallbackQuery, state: FSMContext) -> None:
    # Clear last inline keyboard.
    await clear_last_ikb(user_id=callback.from_user.id, state=state)
    # Enter question.
    await bot.send_message(chat_id=callback.from_user.id, text=ENTER_QUESTION_MESSAGE)
    # Set enter_question state.
    await AddQuestionAndAnswerStatesGroup.enter_question.set()
