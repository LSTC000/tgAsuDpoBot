from data.redis import LAST_IKB_REDIS_KEY

from data.messages import CONFIRM_ALERT_FOR_USERS_MESSAGE

from keyboards import confirm_alert_for_users_menu_ikb

from loader import bot

from aiogram.dispatcher.storage import FSMContext


async def call_confirm_alert_for_users_menu_ikb(user_id: int, text: str, state: FSMContext) -> None:
    """
    :param user_id: Telegram user id.
    :param text: Alert text.
    :param state: FSMContext.
    :return: None.
    """

    async with state.proxy() as data:
        # Call admin inline menu.
        msg = await bot.send_message(
            chat_id=user_id,
            text=CONFIRM_ALERT_FOR_USERS_MESSAGE.format(text),
            reply_markup=confirm_alert_for_users_menu_ikb()
        )
        # Remember id of the last inline keyboard.
        data[LAST_IKB_REDIS_KEY] = msg.message_id
