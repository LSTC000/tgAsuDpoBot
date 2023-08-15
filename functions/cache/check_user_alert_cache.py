from loader import users_alert_cache

from database import check_user_alert


async def check_user_alert_cache(user_id: int) -> bool:
    '''
    :param user_id: Telegram user_id.
    :return: True if the user has enabled alerts, else False.
    '''

    if user_id in users_alert_cache.keys():
        return users_alert_cache[user_id]
    else:
        user_alert = await check_user_alert(user_id)
        users_alert_cache[user_id] = user_alert
        return user_alert
