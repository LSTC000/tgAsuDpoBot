from database import QuestionsAndAnswers


async def update_question(question: str, new_question: str) -> None:
    """
    :param question: Old question.
    :param new_question: New question.
    """

    await QuestionsAndAnswers.update.values(question=new_question) \
        .where(QuestionsAndAnswers.question == question).gino.status()
