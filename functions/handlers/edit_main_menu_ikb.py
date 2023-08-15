from data.redis import LAST_IKB_REDIS_KEY

from keyboards import main_menu_ikb

from loader import bot

from aiogram.dispatcher.storage import FSMContext


async def edit_main_menu_ikb(user_id: int, alert: bool, state: FSMContext) -> None:
    """
    :param user_id: Telegram user id.
    :param alert: True if the user has enabled alerts, else False.
    :param state: FSMContext.
    :return: None.
    """

    async with state.proxy() as data:
        # Edit main inline menu.
        await bot.edit_message_reply_markup(
            chat_id=user_id,
            message_id=data[LAST_IKB_REDIS_KEY],
            reply_markup=main_menu_ikb(alert)
        )
