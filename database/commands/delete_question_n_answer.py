from database import QuestionsAndAnswers


async def delete_question_n_answer(question_id: id) -> None:
    """
    :param question_id: Question id.
    """

    return await QuestionsAndAnswers.delete.where(QuestionsAndAnswers.id == question_id).gino.scalar()
