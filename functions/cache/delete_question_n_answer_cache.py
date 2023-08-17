from loader import questions_cache

from database import delete_question_n_answer, get_questions


async def delete_question_n_answer_cache(question_id: int) -> None:
    """
    :param question_id: Question id.
    :return: None.
    """

    # Delete question and answer from the database.
    await delete_question_n_answer(question_id=question_id)
    # Update questions cache.
    questions_cache['questions'] = {question[0]: question[1] for question in await get_questions()}
