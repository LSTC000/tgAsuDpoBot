from loader import dp

from functions import clear_last_ikb, call_start_ikb

from states import StartCmdStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.message_handler(commands=['start'], state='*')
async def start_cmd(message: types.Message, state: FSMContext) -> None:
    user_id = message.from_user.id

    # Clear last inline keyboard.
    await clear_last_ikb(user_id=user_id, state=state)

    async with state.proxy() as data:
        # Clear all redis data for user.
        data.clear()

    # Call start inline menu.
    await call_start_ikb(user_id=user_id, first_name=message.from_user.first_name, state=state)
    # Set start_ikb state.
    await StartCmdStatesGroup.start_ikb.set()
