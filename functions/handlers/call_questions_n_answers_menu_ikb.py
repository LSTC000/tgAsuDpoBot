from data.redis import LAST_IKB_REDIS_KEY

from data.messages import QUESTIONS_N_ANSWERS_MENU_MESSAGE

from keyboards import questions_n_answers_menu_ikb

from loader import bot

from aiogram.dispatcher.storage import FSMContext


async def call_questions_n_answers_menu_ikb(user_id: int, state: FSMContext) -> None:
    """
    :param user_id: Telegram user id.
    :param state: FSMContext.
    :return: None.
    """

    async with state.proxy() as data:
        # Call questions and answers inline menu.
        msg = await bot.send_message(
            chat_id=user_id,
            text=QUESTIONS_N_ANSWERS_MENU_MESSAGE,
            reply_markup=questions_n_answers_menu_ikb()
        )
        # Remember id of the last inline keyboard.
        data[LAST_IKB_REDIS_KEY] = msg.message_id
