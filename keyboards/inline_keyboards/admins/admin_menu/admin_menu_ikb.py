from data.config import ROW_WIDTH

from data.callbacks import (
    QUESTIONS_N_ANSWERS_CALLBACK_DATA,
    ALERT_FOR_USERS_CALLBACK_DATA,
    CANCEL_TO_MAIN_MENU_CALLBACK_DATA
)

from data.messages import (
    QUESTIONS_N_ANSWERS_IKB_MESSAGE,
    ALERT_FOR_USERS_IKB_MESSAGE,
    CANCEL_TO_MAIN_MENU_IKB_MESSAGE
)

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def admin_menu_ikb() -> InlineKeyboardMarkup:
    """
    :return: Admin menu inline keyboard.
    """

    ikb = InlineKeyboardMarkup(row_width=ROW_WIDTH)

    ikb.row(InlineKeyboardButton(text=QUESTIONS_N_ANSWERS_IKB_MESSAGE, callback_data=QUESTIONS_N_ANSWERS_CALLBACK_DATA))
    ikb.row(InlineKeyboardButton(text=ALERT_FOR_USERS_IKB_MESSAGE, callback_data=ALERT_FOR_USERS_CALLBACK_DATA))
    ikb.row(InlineKeyboardButton(text=CANCEL_TO_MAIN_MENU_IKB_MESSAGE, callback_data=CANCEL_TO_MAIN_MENU_CALLBACK_DATA))

    return ikb
