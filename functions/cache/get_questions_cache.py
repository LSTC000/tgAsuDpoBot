from loader import questions_cache

from database import get_questions


async def get_questions_cache() -> dict:
    """
    :return: Dict with questions and questions id`s.
    """

    if 'questions' in questions_cache.keys():
        return questions_cache['questions']
    else:
        questions = {question[0]: question[1] for question in await get_questions()}
        questions_cache['questions'] = questions
        return questions
