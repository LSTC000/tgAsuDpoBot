from loader import questions_cache

from database import add_question_n_answer, get_questions


async def add_question_n_answer_cache(question: str, answer: str) -> None:
    """
    :param question: Question.
    :param answer: Answer.
    :return: None.
    """

    # Add question and answer the database.
    await add_question_n_answer(question=question, answer=answer)
    # Update questions cache.
    questions_cache['questions'] = {question[0]: question[1] for question in await get_questions()}
