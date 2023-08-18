from data.config import ROW_WIDTH

from data.callbacks import (
    ADD_QUESTION_CALLBACK_DATA,
    ADD_ANSWER_CALLBACK_DATA,
    SAVE_ADD_QUESTION_N_ANSWER_CALLBACK_DATA,
    CANCEL_TO_QUESTIONS_N_ANSWERS_MENU_CALLBACK_DATA
)

from data.messages import (
    ADD_QUESTION_IKB_MESSAGE,
    ADD_ANSWER_IKB_MESSAGE,
    SAVE_ADD_QUESTION_N_ANSWER_IKB_MESSAGE,
    CANCEL_TO_QUESTIONS_N_ANSWERS_MENU_IKB_MESSAGE
)

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def add_question_n_answer_menu_ikb() -> InlineKeyboardMarkup:
    """
    :return: Add question and answer menu inline keyboard.
    """

    ikb = InlineKeyboardMarkup(row_width=ROW_WIDTH)

    ikb.row(InlineKeyboardButton(text=ADD_QUESTION_IKB_MESSAGE, callback_data=ADD_QUESTION_CALLBACK_DATA))
    ikb.row(InlineKeyboardButton(text=ADD_ANSWER_IKB_MESSAGE, callback_data=ADD_ANSWER_CALLBACK_DATA))
    ikb.row(InlineKeyboardButton(
        text=SAVE_ADD_QUESTION_N_ANSWER_IKB_MESSAGE,
        callback_data=SAVE_ADD_QUESTION_N_ANSWER_CALLBACK_DATA)
    )
    ikb.row(InlineKeyboardButton(
        text=CANCEL_TO_QUESTIONS_N_ANSWERS_MENU_IKB_MESSAGE,
        callback_data=CANCEL_TO_QUESTIONS_N_ANSWERS_MENU_CALLBACK_DATA)
    )

    return ikb
