from data.redis import LAST_IKB_REDIS_KEY

from data.messages import MAIN_MENU_MESSAGE

from functions import check_user_alert_cache

from keyboards import main_menu_ikb

from loader import bot

from aiogram.dispatcher.storage import FSMContext


async def call_main_menu_ikb(user_id: int, state: FSMContext) -> None:
    """
    :param user_id: Telegram user id.
    :param state: FSMContext.
    :return: None.
    """

    async with state.proxy() as data:
        # Call main inline menu.
        msg = await bot.send_message(
            chat_id=user_id,
            text=MAIN_MENU_MESSAGE,
            reply_markup=main_menu_ikb(await check_user_alert_cache(user_id))
        )
        # Remember id of the last inline keyboard.
        data[LAST_IKB_REDIS_KEY] = msg.message_id
