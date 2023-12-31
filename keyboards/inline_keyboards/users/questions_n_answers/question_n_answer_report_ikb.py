from data.config import ROW_WIDTH

from data.callbacks import CANCEL_TO_MAIN_MENU_CALLBACK_DATA, CANCEL_TO_QUESTIONS_N_ANSWERS_CALLBACK_DATA

from data.messages import CANCEL_TO_MAIN_MENU_IKB_MESSAGE, CANCEL_TO_QUESTIONS_N_ANSWERS_IKB_MESSAGE

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def question_n_answer_report_ikb() -> InlineKeyboardMarkup:
    """
    :return: Question and answer inline keyboard.
    """

    ikb = InlineKeyboardMarkup(row_width=ROW_WIDTH)

    ikb.row(InlineKeyboardButton(
        text=CANCEL_TO_QUESTIONS_N_ANSWERS_IKB_MESSAGE,
        callback_data=CANCEL_TO_QUESTIONS_N_ANSWERS_CALLBACK_DATA)
    )
    ikb.row(InlineKeyboardButton(text=CANCEL_TO_MAIN_MENU_IKB_MESSAGE, callback_data=CANCEL_TO_MAIN_MENU_CALLBACK_DATA))

    return ikb
