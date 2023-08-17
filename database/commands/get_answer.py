from database import QuestionsAndAnswers

from sqlalchemy import select
from sqlalchemy.exc import ArgumentError


async def get_answer(question_id: int) -> str:
    """
    :param question_id: Question id.
    :return: Answer.
    """

    try:
        answer = await select([QuestionsAndAnswers.answer]).where(QuestionsAndAnswers.id == question_id).gino.all()
        return answer[0][0]
    except ArgumentError:
        return ''
