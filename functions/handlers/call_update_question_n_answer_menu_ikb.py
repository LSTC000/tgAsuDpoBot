from data.redis import LAST_IKB_REDIS_KEY

from data.messages import UPDATE_QUESTION_N_ANSWER_MENU_MESSAGE

from keyboards import update_question_n_answer_menu_ikb

from loader import bot

from aiogram.dispatcher.storage import FSMContext


async def call_update_question_n_answer_menu_ikb(user_id: int, state: FSMContext) -> None:
    """
    :param user_id: Telegram user id.
    :param state: FSMContext.
    :return: None.
    """

    async with state.proxy() as data:
        # Call update question and answer inline menu.
        msg = await bot.send_message(
            chat_id=user_id,
            text=UPDATE_QUESTION_N_ANSWER_MENU_MESSAGE,
            reply_markup=update_question_n_answer_menu_ikb()
        )
        # Remember id of the last inline keyboard.
        data[LAST_IKB_REDIS_KEY] = msg.message_id
