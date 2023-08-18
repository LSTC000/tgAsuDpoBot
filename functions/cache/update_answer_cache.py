from loader import questions_cache

from database import update_answer, get_questions


async def update_answer_cache(question_id: int, new_answer: str) -> None:
    """
    :param question_id: Question id.
    :param new_answer: New answer.
    :return: None.
    """

    # Update question in the database.
    await update_answer(question_id=question_id, new_answer=new_answer)
    # Update questions cache.
    questions_cache['questions'] = {question[0]: question[1] for question in await get_questions()}
