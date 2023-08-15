from loader import dp

from data.callbacks import CHANGE_USER_ALERT_CALLBACK_DATA

from functions import edit_main_menu_ikb, check_user_alert_cache, add_user_alert_cache, delete_user_alert_cache

from states import MainMenuStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(lambda c: c.data == CHANGE_USER_ALERT_CALLBACK_DATA, state=MainMenuStatesGroup.main_menu_ikb)
async def change_user_alert(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    # Check if the user has alerts enabled.
    # If enabled, then turn them off, otherwise turn them on.
    alert = await check_user_alert_cache(user_id)
    if alert:
        await delete_user_alert_cache(user_id)
    else:
        await add_user_alert_cache(user_id)

    # Edit alert in the main inline keyboard menu.
    await edit_main_menu_ikb(user_id=user_id, alert=not(alert), state=state)
