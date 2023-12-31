from loader import dp, bot

from data.callbacks import ALERT_FOR_USERS_CALLBACK_DATA

from data.messages import ENTER_ALERT_FOR_USERS_MESSAGE

from functions import clear_last_ikb

from states import AdminMenuStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(lambda c: c.data == ALERT_FOR_USERS_CALLBACK_DATA, state=AdminMenuStatesGroup.admin_menu)
async def alert_for_users(callback: types.CallbackQuery, state: FSMContext) -> None:
    # Clear last inline keyboard.
    await clear_last_ikb(user_id=callback.from_user.id, state=state)
    # Enter alert for users.
    await bot.send_message(chat_id=callback.from_user.id, text=ENTER_ALERT_FOR_USERS_MESSAGE)
    # Set alert_for_users state.
    await AdminMenuStatesGroup.enter_alert_for_users.set()
