from data.config import ROW_WIDTH

from data.callbacks import CONFIRM_ADD_QUESTION_N_ANSWER_CALLBACK_DATA, CANCEL_ADD_QUESTION_N_ANSWER_CALLBACK_DATA

from data.messages import CONFIRM_ADD_QUESTION_N_ANSWER_IKB_MESSAGE, CANCEL_ADD_QUESTION_N_ANSWER_IKB_MESSAGE

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def confirm_add_question_n_answer_menu_ikb() -> InlineKeyboardMarkup:
    """
    :return: Confirm question and answer menu inline keyboard.
    """

    ikb = InlineKeyboardMarkup(row_width=ROW_WIDTH)

    ikb.row(InlineKeyboardButton(
        text=CONFIRM_ADD_QUESTION_N_ANSWER_IKB_MESSAGE,
        callback_data=CONFIRM_ADD_QUESTION_N_ANSWER_CALLBACK_DATA)
    )
    ikb.row(InlineKeyboardButton(
        text=CANCEL_ADD_QUESTION_N_ANSWER_IKB_MESSAGE,
        callback_data=CANCEL_ADD_QUESTION_N_ANSWER_CALLBACK_DATA)
    )

    return ikb
