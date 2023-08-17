from database import QuestionsAndAnswers


async def update_question(question_id: int, new_question: str) -> None:
    """
    :param question_id: Question id.
    :param new_question: New question.
    """

    await QuestionsAndAnswers.update.values(question=new_question) \
        .where(QuestionsAndAnswers.id == question_id).gino.status()
