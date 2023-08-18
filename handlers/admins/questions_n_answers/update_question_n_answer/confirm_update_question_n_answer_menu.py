from loader import dp

from data.callbacks import CONFIRM_UPDATE_QUESTION_N_ANSWER_CALLBACK_DATA, CANCEL_UPDATE_QUESTION_N_ANSWER_CALLBACK_DATA

from data.messages import SUCCESSFUL_UPDATE_QUESTION_N_ANSWER_MESSAGE

from data.redis import (
    PICKER_PAGE_REDIS_KEY,
    ADMIN_MENU_REDIS_KEY,
    QUESTION_REDIS_KEY,
    QUESTION_ID_REDIS_KEY,
    ANSWER_REDIS_KEY
)

from functions import (
    clear_last_ikb,
    call_questions_n_answers_menu_ikb,
    call_update_question_n_answer_menu_ikb,
    update_question_cache,
    update_answer_cache
)

from states import UpdateQuestionAndAnswerStatesGroup, QuestionsAndAnswersMenuStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(
    lambda c: c.data in [CONFIRM_UPDATE_QUESTION_N_ANSWER_CALLBACK_DATA, CANCEL_UPDATE_QUESTION_N_ANSWER_CALLBACK_DATA],
    state=UpdateQuestionAndAnswerStatesGroup.confirm_update_question_n_answer_menu
)
async def confirm_update_question_n_answer_menu(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    # Clear last inline keyboard.
    await clear_last_ikb(user_id=user_id, state=state)

    if callback.data == CONFIRM_UPDATE_QUESTION_N_ANSWER_CALLBACK_DATA:
        async with state.proxy() as data:
            question_id = int(data[QUESTION_ID_REDIS_KEY])

            data.pop(PICKER_PAGE_REDIS_KEY)
            data.pop(ADMIN_MENU_REDIS_KEY)

            if QUESTION_REDIS_KEY in data:
                await update_question_cache(question_id=question_id, new_question=data.pop(QUESTION_REDIS_KEY))

            if ANSWER_REDIS_KEY in data:
                await update_answer_cache(question_id=question_id, new_answer=data.pop(ANSWER_REDIS_KEY))

        await callback.answer(text=SUCCESSFUL_UPDATE_QUESTION_N_ANSWER_MESSAGE, show_alert=True)

        # Call questions and answers menu.
        await call_questions_n_answers_menu_ikb(user_id=user_id, state=state)
        # Set questions_n_answers_menu state.
        await QuestionsAndAnswersMenuStatesGroup.questions_n_answers_menu.set()
    else:
        # Call update question and answer inline menu.
        await call_update_question_n_answer_menu_ikb(user_id=user_id, state=state)
        # Set update_question_n_answer_menu state.
        await UpdateQuestionAndAnswerStatesGroup.update_question_n_answer_menu.set()
