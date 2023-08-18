from math import ceil

from data.callbacks import (
    CANCEL_TO_MAIN_MENU_CALLBACK_DATA,
    CANCEL_TO_ADMIN_MENU_CALLBACK_DATA,
    IGNORE_CALLBACK_DATA,
    PREV_CALLBACK_DATA,
    NEXT_CALLBACK_DATA
)

from data.config import QUESTIONS_AND_ANSWERS_PICKER_ROW_WIDTH, MAX_QUESTIONS_ON_PAGE

from data.messages import CANCEL_TO_MAIN_MENU_IKB_MESSAGE, CANCEL_TO_ADMIN_MENU_IKB_MESSAGE

from data.redis import PICKER_PAGE_REDIS_KEY, ADMIN_MENU_REDIS_KEY

from functions import get_questions_cache

from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class QuestionsAndAnswersPicker:
    async def start_picker(self, page: int, admin_menu: bool = False) -> InlineKeyboardMarkup:
        """
        :param page: Current picker page. Start value: 0.
        :param admin_menu: True if the user is in the admin menu. Default: False.
        :return: Inline keyboard for pick a question and answer.
        """

        ikb = InlineKeyboardMarkup(row_width=QUESTIONS_AND_ANSWERS_PICKER_ROW_WIDTH)

        questions = await get_questions_cache()
        questions_count = len(questions)

        start = page * MAX_QUESTIONS_ON_PAGE
        stop = start + MAX_QUESTIONS_ON_PAGE if start + MAX_QUESTIONS_ON_PAGE <= questions_count else questions_count

        for key in list(questions.keys())[start:stop]:
            ikb.row(
                InlineKeyboardButton(
                    text=questions[key],
                    callback_data=key
                )
            )

        ikb.row()
        ikb.insert(
            InlineKeyboardButton(
                text="<<" if page != 0 else " ",
                callback_data=PREV_CALLBACK_DATA if page != 0 else IGNORE_CALLBACK_DATA
            )
        )
        ikb.insert(
            InlineKeyboardButton(
                f"{page+1}/{ceil(questions_count / MAX_QUESTIONS_ON_PAGE)}",
                callback_data=IGNORE_CALLBACK_DATA
            )
        )
        ikb.insert(
            InlineKeyboardButton(
                text=">>" if questions_count > stop else " ",
                callback_data=NEXT_CALLBACK_DATA if questions_count > stop else IGNORE_CALLBACK_DATA)
        )

        if admin_menu:
            ikb.row(InlineKeyboardButton(
                CANCEL_TO_ADMIN_MENU_IKB_MESSAGE, callback_data=CANCEL_TO_ADMIN_MENU_CALLBACK_DATA)
            )
        else:
            ikb.row(InlineKeyboardButton(
                CANCEL_TO_MAIN_MENU_IKB_MESSAGE, callback_data=CANCEL_TO_MAIN_MENU_CALLBACK_DATA)
            )

        return ikb

    async def process_selection(
            self,
            callback: types.CallbackQuery,
            callback_data: str,
            state: FSMContext
    ) -> tuple:
        """
        :param callback: Callback query the last picker inline keyboard.
        :param callback_data: Callback query data the last picker inline keyboard.
        :param state: FSMContext.
        :return: A tuple consisting of two values: whether the user has chosen a question (Default: False)
        and the id of this question (Default: None).
        """

        async with state.proxy() as data:
            page = data[PICKER_PAGE_REDIS_KEY]

            return_data = False, None

            if callback_data == IGNORE_CALLBACK_DATA:
                await callback.answer(cache_time=60)
            elif callback_data == PREV_CALLBACK_DATA:
                page -= 1
                data[PICKER_PAGE_REDIS_KEY] = page
                await callback.message.edit_reply_markup(
                    reply_markup=await self.start_picker(page=page, admin_menu=data[ADMIN_MENU_REDIS_KEY])
                )
            elif callback_data == NEXT_CALLBACK_DATA:
                page += 1
                data[PICKER_PAGE_REDIS_KEY] = page
                await callback.message.edit_reply_markup(
                    reply_markup=await self.start_picker(page=page, admin_menu=data[ADMIN_MENU_REDIS_KEY])
                )
            elif callback_data != CANCEL_TO_MAIN_MENU_CALLBACK_DATA:
                return_data = True, callback_data

        return return_data
