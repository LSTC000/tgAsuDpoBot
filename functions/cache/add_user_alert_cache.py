from loader import users_alert_cache

from database import add_user_alert


async def add_user_alert_cache(user_id: int) -> None:
    '''
    :param user_id: Telegram user_id.
    :return: None.
    '''

    # Add user in the database.
    await add_user_alert(user_id)
    # Change or add alert value.
    users_alert_cache[user_id] = True
