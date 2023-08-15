from typing import Union

from database import get_users_alert

from loader import bot

from aiogram.utils.exceptions import (
    BotBlocked,
    ChatNotFound,
    UserDeactivated,
    MigrateToChat,
    Unauthorized,
    BadRequest,
    RetryAfter
)


async def send_alert(
    text_alert: str,
    disable_notification: bool = True,
    users_alert: Union[list, None] = None
) -> None:
    '''
    :param text_alert: Text for alert.
    :param disable_notification: Disable notification (check aiogram documentation).
    :param users_alert: Telegram users id for alert. Example: [[user_id], [user_id], ...].
    :return: None.
    '''

    if users_alert is None:
        users_alert = await get_users_alert()

    for user_alert in users_alert:
        user_alert = user_alert[0]
        try:
            await bot.send_message(
                chat_id=user_alert,
                text=text_alert,
                disable_notification=disable_notification
            )
        except (BotBlocked, ChatNotFound, UserDeactivated, MigrateToChat, Unauthorized, BadRequest, RetryAfter):
            pass
