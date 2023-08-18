from loader import dp

from data.callbacks import CONFIRM_ADD_QUESTION_N_ANSWER_CALLBACK_DATA, CANCEL_ADD_QUESTION_N_ANSWER_CALLBACK_DATA

from data.messages import SUCCESSFUL_ADD_QUESTION_N_ANSWER_MESSAGE

from data.redis import QUESTION_REDIS_KEY, ANSWER_REDIS_KEY

from functions import (
    clear_last_ikb,
    call_admin_menu_ikb,
    call_add_question_n_answer_menu_ikb,
    add_question_n_answer_cache
)

from states import AdminMenuStatesGroup, AddQuestionAndAnswerStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(
    lambda c: c.data in [CONFIRM_ADD_QUESTION_N_ANSWER_CALLBACK_DATA, CANCEL_ADD_QUESTION_N_ANSWER_CALLBACK_DATA],
    state=AddQuestionAndAnswerStatesGroup.confirm_add_question_n_answer_menu
)
async def confirm_add_question_n_answer_menu(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    # Clear last inline keyboard.
    await clear_last_ikb(user_id=user_id, state=state)

    if callback.data == CONFIRM_ADD_QUESTION_N_ANSWER_CALLBACK_DATA:
        async with state.proxy() as data:
            question, answer = data.pop(QUESTION_REDIS_KEY), data.pop(ANSWER_REDIS_KEY)
            await add_question_n_answer_cache(question=question, answer=answer)

        await callback.answer(text=SUCCESSFUL_ADD_QUESTION_N_ANSWER_MESSAGE, show_alert=True)

        # Call admin menu.
        await call_admin_menu_ikb(user_id=user_id, state=state)
        # Set admin_menu state.
        await AdminMenuStatesGroup.admin_menu.set()
    else:
        # Call add question and answer inline menu.
        await call_add_question_n_answer_menu_ikb(user_id=user_id, state=state)
        # Set add_question_n_answer_menu state.
        await AddQuestionAndAnswerStatesGroup.add_question_n_answer_menu.set()
