from loader import dp, bot

from data.callbacks import DELETE_QUESTION_N_ANSWER_CALLBACK_DATA

from data.messages import DELETE_QUESTION_N_ANSWER_MESSAGE

from data.redis import PICKER_PAGE_REDIS_KEY, ADMIN_MENU_REDIS_KEY, LAST_IKB_REDIS_KEY

from functions import clear_last_ikb

from pickers import QuestionsAndAnswersPicker

from states import QuestionsAndAnswersMenuStatesGroup, DeleteQuestionAndAnswerStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(
    lambda c: c.data == DELETE_QUESTION_N_ANSWER_CALLBACK_DATA,
    state=QuestionsAndAnswersMenuStatesGroup.questions_n_answers_menu
)
async def delete_question_n_answer_picker(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    # Clear last inline keyboard.
    await clear_last_ikb(user_id=user_id, state=state)

    async with state.proxy() as data:
        data[PICKER_PAGE_REDIS_KEY] = 0
        data[ADMIN_MENU_REDIS_KEY] = True

        # Call questions and answers picker inline menu.
        msg = await bot.send_message(
            chat_id=user_id,
            text=DELETE_QUESTION_N_ANSWER_MESSAGE,
            reply_markup=await QuestionsAndAnswersPicker().start_picker(admin_menu=True)
        )
        # Remember id of the last inline keyboard.
        data[LAST_IKB_REDIS_KEY] = msg.message_id

    # Set process_delete_question_n_answer_picker state.
    await DeleteQuestionAndAnswerStatesGroup.process_delete_question_n_answer_picker.set()

