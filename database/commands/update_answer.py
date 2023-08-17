from database import QuestionsAndAnswers


async def update_answer(question_id: int, new_answer: str) -> None:
    """
    :param question_id: Question id.
    :param new_answer: New answer.
    """

    await QuestionsAndAnswers.update.values(answer=new_answer) \
        .where(QuestionsAndAnswers.id == question_id).gino.status()
