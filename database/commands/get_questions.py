from database import QuestionsAndAnswers

from sqlalchemy import select
from sqlalchemy.exc import ArgumentError


async def get_questions() -> list:
    """
    :return: List with questions and questions id`s.
    """

    try:
        return await select([QuestionsAndAnswers.id, QuestionsAndAnswers.question]).gino.all()
    except ArgumentError:
        return []
