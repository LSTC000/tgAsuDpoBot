from database import QuestionsAndAnswers

from sqlalchemy import select
from sqlalchemy.exc import ArgumentError


async def get_answer(question: str) -> str:
    """
    :param question: Question.
    :return: Answer.
    """

    try:
        answer = await select([QuestionsAndAnswers.answer]).gino.all()
        return answer[0][0]
    except ArgumentError:
        return ''
