from database import QuestionsAndAnswers


async def delete_question_n_answer(question: str) -> None:
    """
    :param question: Question.
    """

    return await QuestionsAndAnswers.delete.where(QuestionsAndAnswers.question == question).gino.scalar()
