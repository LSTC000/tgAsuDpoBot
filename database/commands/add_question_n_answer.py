from loader import logger

from asyncpg import UniqueViolationError

from database import QuestionsAndAnswers


async def add_question_n_answer(question: str, answer: str) -> None:
    """
    :param question: Question.
    :param answer: Answer.
    :return: None.
    """

    try:
        question_n_answer = QuestionsAndAnswers(question=question, answer=answer)
        await question_n_answer.create()
    except UniqueViolationError:
        logger.info('Error to question and answer! Question and answer already exists in the database.')
