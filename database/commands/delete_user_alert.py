from database import Alerts


async def delete_user_alert(user_id: int) -> None:
    """
    :param user_id: Telegram user id.
    :return: None.
    """

    return await Alerts.delete.where(Alerts.user_id == user_id).gino.scalar()
