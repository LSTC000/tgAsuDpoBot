from database import QuestionsAndAnswers


async def update_answer(question: str, new_answer: str) -> None:
    """
    :param question: Question.
    :param new_answer: New answer.
    """

    await QuestionsAndAnswers.update.values(answer=new_answer) \
        .where(QuestionsAndAnswers.question == question).gino.status()
