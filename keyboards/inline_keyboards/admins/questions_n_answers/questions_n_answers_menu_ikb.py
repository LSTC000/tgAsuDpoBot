from data.config import ROW_WIDTH

from data.callbacks import (
    ADD_QUESTION_N_ANSWER_CALLBACK_DATA,
    UPDATE_QUESTION_N_ANSWER_CALLBACK_DATA,
    DELETE_QUESTION_N_ANSWER_CALLBACK_DATA,
    CANCEL_TO_ADMIN_MENU_CALLBACK_DATA
)

from data.messages import (
    ADD_QUESTION_N_ANSWER_IKB_MESSAGE,
    UPDATE_QUESTION_N_ANSWER_IKB_MESSAGE,
    DELETE_QUESTION_N_ANSWER_IKB_MESSAGE,
    CANCEL_TO_ADMIN_MENU_IKB_MESSAGE
)

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def questions_n_answers_menu_ikb() -> InlineKeyboardMarkup:
    """
    :return: Questions and answers menu inline keyboard.
    """

    ikb = InlineKeyboardMarkup(row_width=ROW_WIDTH)

    ikb.row(InlineKeyboardButton(
        text=ADD_QUESTION_N_ANSWER_IKB_MESSAGE,
        callback_data=ADD_QUESTION_N_ANSWER_CALLBACK_DATA)
    )
    ikb.row(InlineKeyboardButton(
        text=UPDATE_QUESTION_N_ANSWER_IKB_MESSAGE,
        callback_data=UPDATE_QUESTION_N_ANSWER_CALLBACK_DATA)
    )
    ikb.row(InlineKeyboardButton(
        text=DELETE_QUESTION_N_ANSWER_IKB_MESSAGE,
        callback_data=DELETE_QUESTION_N_ANSWER_CALLBACK_DATA)
    )
    ikb.row(InlineKeyboardButton(
        text=CANCEL_TO_ADMIN_MENU_IKB_MESSAGE,
        callback_data=CANCEL_TO_ADMIN_MENU_CALLBACK_DATA)
    )

    return ikb
