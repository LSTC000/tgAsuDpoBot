from loader import dp, bot

from data.callbacks import UPDATE_QUESTION_CALLBACK_DATA

from data.messages import ENTER_NEW_QUESTION_MESSAGE

from functions import clear_last_ikb

from states import UpdateQuestionAndAnswerStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(
    lambda c: c.data == UPDATE_QUESTION_CALLBACK_DATA,
    state=UpdateQuestionAndAnswerStatesGroup.update_question_n_answer_menu
)
async def update_question(callback: types.CallbackQuery, state: FSMContext) -> None:
    # Clear last inline keyboard.
    await clear_last_ikb(user_id=callback.from_user.id, state=state)
    # Enter new question.
    await bot.send_message(chat_id=callback.from_user.id, text=ENTER_NEW_QUESTION_MESSAGE)
    # Set enter_new_question state.
    await UpdateQuestionAndAnswerStatesGroup.enter_new_question.set()
