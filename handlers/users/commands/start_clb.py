from loader import dp

from data.callbacks import START_COMMAND_CALLBACK_DATA

from functions import clear_last_ikb, call_main_menu_ikb, check_user_alert_cache

from states import StartCmdStatesGroup, MainMenuStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(lambda c: c.data == START_COMMAND_CALLBACK_DATA, state=StartCmdStatesGroup.start_ikb)
async def start_clb(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    # Clear last inline keyboard.
    await clear_last_ikb(user_id=user_id, state=state)
    # Call main inline menu.
    await call_main_menu_ikb(user_id=user_id, alert=await check_user_alert_cache(user_id), state=state)
    # Set main_menu_ikb state.
    await MainMenuStatesGroup.main_menu.set()
