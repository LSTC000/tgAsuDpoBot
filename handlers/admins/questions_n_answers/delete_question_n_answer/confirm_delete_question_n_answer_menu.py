from loader import dp

from data.callbacks import CONFIRM_DELETE_QUESTION_N_ANSWER_CALLBACK_DATA, CANCEL_DELETE_QUESTION_N_ANSWER_CALLBACK_DATA

from data.messages import SUCCESSFUL_DELETE_QUESTION_N_ANSWER_MESSAGE

from data.redis import QUESTION_REDIS_KEY, QUESTION_ID_REDIS_KEY, ADMIN_MENU_REDIS_KEY, PICKER_PAGE_REDIS_KEY

from functions import clear_last_ikb, call_questions_n_answers_menu_ikb, delete_question_n_answer_cache

from states import DeleteQuestionAndAnswerStatesGroup, QuestionsAndAnswersMenuStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(
    lambda c: c.data in [CONFIRM_DELETE_QUESTION_N_ANSWER_CALLBACK_DATA, CANCEL_DELETE_QUESTION_N_ANSWER_CALLBACK_DATA],
    state=DeleteQuestionAndAnswerStatesGroup.confirm_delete_question_n_answer_menu
)
async def confirm_delete_question_n_answer_menu(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    # Clear last inline keyboard.
    await clear_last_ikb(user_id=user_id, state=state)

    if callback.data == CONFIRM_DELETE_QUESTION_N_ANSWER_CALLBACK_DATA:
        async with state.proxy() as data:
            data.pop(QUESTION_REDIS_KEY)
            data.pop(PICKER_PAGE_REDIS_KEY)
            data.pop(ADMIN_MENU_REDIS_KEY)

            await delete_question_n_answer_cache(int(data.pop(QUESTION_ID_REDIS_KEY)))

        await callback.answer(text=SUCCESSFUL_DELETE_QUESTION_N_ANSWER_MESSAGE, show_alert=True)

    # Call questions and answers menu.
    await call_questions_n_answers_menu_ikb(user_id=user_id, state=state)
    # Set questions_n_answers_menu state.
    await QuestionsAndAnswersMenuStatesGroup.questions_n_answers_menu.set()
