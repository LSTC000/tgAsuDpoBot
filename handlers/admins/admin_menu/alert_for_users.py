from loader import dp, bot

from data.callbacks import (
    ALERT_FOR_USERS_CALLBACK_DATA,
    CONFIRM_ALERT_FOR_USERS_CALLBACK_DATA,
    CANCEL_ALERT_FOR_USERS_CALLBACK_DATA
)

from data.messages import ALERT_FOR_USERS_MESSAGE, ERROR_ALERT_FOR_USERS_MESSAGE, SUCCESSFULLY_ALERT_FOR_USERS_MESSAGE

from data.redis import ALERT_FOR_USERS_REDIS_KEY

from functions import clear_last_ikb, send_alerts, call_admin_menu_ikb, call_confirm_alert_for_users_menu_ikb

from utils import Validator

from states import AdminMenuStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(lambda c: c.data == ALERT_FOR_USERS_CALLBACK_DATA, state=AdminMenuStatesGroup.admin_menu)
async def enter_alert_for_users(callback: types.CallbackQuery) -> None:
    # Enter alert for users.
    await bot.send_message(chat_id=callback.from_user.id, text=ALERT_FOR_USERS_MESSAGE)
    # Set alert_for_users state.
    await AdminMenuStatesGroup.alert_for_users.set()


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=AdminMenuStatesGroup.alert_for_users)
async def alert_for_users(message: types.Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    text = message.text

    # Clear last inline keyboard.
    await clear_last_ikb(user_id=user_id, state=state)
    # Check alert on valid.
    if Validator().alert_validation(text):
        async with state.proxy() as data:
            data[ALERT_FOR_USERS_REDIS_KEY] = text
        # Call confirm menu.
        await call_confirm_alert_for_users_menu_ikb(user_id=user_id, text=text, state=state)
        # Set confirm_alert_for_users state.
        await AdminMenuStatesGroup.confirm_alert_for_users.set()
    else:
        await bot.send_message(chat_id=user_id, text=ERROR_ALERT_FOR_USERS_MESSAGE)
        # Call admin menu.
        await call_admin_menu_ikb(user_id=user_id, state=state)
        # Set admin_menu state.
        await AdminMenuStatesGroup.admin_menu.set()


@dp.callback_query_handler(
    lambda c: c.data in [CONFIRM_ALERT_FOR_USERS_CALLBACK_DATA, CANCEL_ALERT_FOR_USERS_CALLBACK_DATA],
    state=AdminMenuStatesGroup.confirm_alert_for_users
)
async def confirm_alert_for_users(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    async with state.proxy() as data:
        text = data[ALERT_FOR_USERS_REDIS_KEY]
        data.pop(ALERT_FOR_USERS_REDIS_KEY)

    if callback.data == CONFIRM_ALERT_FOR_USERS_CALLBACK_DATA:
        # Sending users alert.
        await send_alerts(text_alert=text)
        await bot.send_message(chat_id=user_id, text=SUCCESSFULLY_ALERT_FOR_USERS_MESSAGE)

    # Clear last inline keyboard.
    await clear_last_ikb(user_id=user_id, state=state)
    # Call admin menu.
    await call_admin_menu_ikb(user_id=user_id, state=state)
    # Set admin_menu state.
    await AdminMenuStatesGroup.admin_menu.set()
