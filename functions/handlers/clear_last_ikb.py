from data.redis import LAST_IKB_REDIS_KEY

from loader import bot

from aiogram.dispatcher.storage import FSMContext
from aiogram.utils.exceptions import MessageToDeleteNotFound, MessageCantBeDeleted, MessageNotModified


async def clear_last_ikb(user_id: int, state: FSMContext) -> None:
    '''
    :param user_id: Telegram user id.
    :param state: FSMContext.
    :return: None.
    '''

    async with state.proxy() as data:
        if LAST_IKB_REDIS_KEY in data:
            try:
                await bot.delete_message(chat_id=user_id, message_id=data[LAST_IKB_REDIS_KEY])
            except (MessageToDeleteNotFound, MessageCantBeDeleted, MessageNotModified):
                pass
