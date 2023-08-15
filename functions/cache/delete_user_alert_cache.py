from loader import users_alert_cache

from database import delete_user_alert


async def delete_user_alert_cache(user_id: int) -> None:
    '''
    :param user_id: Telegram user_id.
    :return: None.
    '''

    # Delete user in the database.
    await delete_user_alert(user_id)
    # Change or add alert value.
    users_alert_cache[user_id] = False
