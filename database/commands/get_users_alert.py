from database import Alerts

from sqlalchemy import select
from sqlalchemy.exc import ArgumentError


async def get_users_alert() -> list:
    """
    :return: A list with users who have enabled notifications.
    """

    try:
        return await select([Alerts.user_id]).gino.all()
    except ArgumentError:
        return []
