from database import Alerts


async def check_user_alert(user_id: int) -> bool:
    """
    :param user_id: Telegram user id.
    :return: True if the user has enabled alerts, else False.
    """

    return True if await Alerts.query.where(Alerts.user_id == user_id).gino.all() else False
