from data.redis import (
    PICKER_PAGE_REDIS_KEY,
    ALERT_FOR_USERS_REDIS_KEY,
    QUESTION_REDIS_KEY,
    ANSWER_REDIS_KEY,
    QUESTION_ID_REDIS_KEY,
)

from aiogram.dispatcher.storage import FSMContext


async def clear_redis_data(state: FSMContext) -> None:
    """
    :param state: FSMContext.
    :return: None.
    """

    async with state.proxy() as data:
        if PICKER_PAGE_REDIS_KEY in data:
            data.pop(PICKER_PAGE_REDIS_KEY)

        if ALERT_FOR_USERS_REDIS_KEY in data:
            data.pop(ALERT_FOR_USERS_REDIS_KEY)

        if QUESTION_REDIS_KEY in data:
            data.pop(QUESTION_REDIS_KEY)

        if QUESTION_ID_REDIS_KEY in data:
            data.pop(QUESTION_ID_REDIS_KEY)

        if ANSWER_REDIS_KEY in data:
            data.pop(ANSWER_REDIS_KEY)
