from loader import dp, bot

from data.callbacks import QUESTIONS_N_ANSWERS_CALLBACK_DATA

from data.messages import QUESTIONS_N_ANSWERS_MESSAGE

from data.redis import PICKER_PAGE_REDIS_KEY, ADMIN_MENU_REDIS_KEY, LAST_IKB_REDIS_KEY

from functions import clear_last_ikb

from pickers import QuestionsAndAnswersPicker

from states import MainMenuStatesGroup, QuestionsAndAnswersPickerStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(lambda c: c.data == QUESTIONS_N_ANSWERS_CALLBACK_DATA, state=MainMenuStatesGroup.main_menu)
async def questions_n_answers_picker(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    # Clear last inline keyboard.
    await clear_last_ikb(user_id=user_id, state=state)

    async with state.proxy() as data:
        data[PICKER_PAGE_REDIS_KEY] = 0
        data[ADMIN_MENU_REDIS_KEY] = False

        # Call questions and answers picker inline menu.
        msg = await bot.send_message(
            chat_id=user_id,
            text=QUESTIONS_N_ANSWERS_MESSAGE,
            reply_markup=await QuestionsAndAnswersPicker().start_picker()
        )
        # Remember id of the last inline keyboard.
        data[LAST_IKB_REDIS_KEY] = msg.message_id

    # Set process_questions_n_answers_picker state.
    await QuestionsAndAnswersPickerStatesGroup.process_questions_n_answers_picker.set()

