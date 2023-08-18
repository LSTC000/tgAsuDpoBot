from data.redis import LAST_IKB_REDIS_KEY, QUESTION_ID_REDIS_KEY

from data.messages import CONFIRM_UPDATE_QUESTION_N_ANSWER_MESSAGE

from keyboards import confirm_update_question_n_answer_menu_ikb

from functions import get_questions_cache

from loader import bot

from aiogram.dispatcher.storage import FSMContext


async def call_confirm_update_question_n_answer_menu_ikb(user_id: int, state: FSMContext) -> None:
    """
    :param user_id: Telegram user id.
    :param state: FSMContext.
    :return: None.
    """

    questions = await get_questions_cache()

    async with state.proxy() as data:
        # Call confirm update question and answer inline menu.
        msg = await bot.send_message(
            chat_id=user_id,
            text=CONFIRM_UPDATE_QUESTION_N_ANSWER_MESSAGE.format(questions[int(data[QUESTION_ID_REDIS_KEY])]),
            reply_markup=confirm_update_question_n_answer_menu_ikb()
        )
        # Remember id of the last inline keyboard.
        data[LAST_IKB_REDIS_KEY] = msg.message_id
