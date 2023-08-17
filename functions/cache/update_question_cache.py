from loader import questions_cache

from database import update_question, get_questions


async def update_question_cache(question_id: int, new_question: str) -> None:
    """
    :param question_id: Question id.
    :param new_question: New question.
    :return: None.
    """

    # Update question in the database.
    await update_question(question_id=question_id, new_question=new_question)
    # Update questions cache.
    questions_cache['questions'] = {question[0]: question[1] for question in await get_questions()}
