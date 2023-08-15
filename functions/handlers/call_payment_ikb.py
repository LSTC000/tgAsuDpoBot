from data.redis import LAST_IKB_REDIS_KEY

from data.messages import PAYMENT_DESCRIPTION_MESSAGE

from keyboards import payment_ikb

from loader import bot

from aiogram.dispatcher.storage import FSMContext


async def call_payment_ikb(user_id: int, redirected_url: str, amount: int, state: FSMContext) -> None:
    """
    :param user_id: Telegram user id.
    :param redirected_url: YooMoney redirected url.
    :param amount: Sum to pay.
    :param state: FSMContext.
    :return: None.
    """

    async with state.proxy() as data:
        # Call payment inline menu.
        msg = await bot.send_message(
            chat_id=user_id,
            text=PAYMENT_DESCRIPTION_MESSAGE.format(amount),
            reply_markup=payment_ikb(redirected_url)
        )
        # Remember id of the last inline keyboard.
        data[LAST_IKB_REDIS_KEY] = msg.message_id
