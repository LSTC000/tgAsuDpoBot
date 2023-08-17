import datetime

from database.database_setup import BaseModel

from sqlalchemy import Column, BigInteger, VARCHAR, TEXT, sql, DateTime, func


class QuestionsAndAnswers(BaseModel):
    __tablename__ = 'questions_n_answers'

    # Autoincrement id.
    id = Column(BigInteger, primary_key=True, autoincrement=True,
                server_default=sql.text('nextval(\'questions_n_answers_id_seq\')'))
    # Question.
    question = Column(VARCHAR(128), nullable=False)
    # Answer.
    answer = Column(TEXT, nullable=False)
    # Created question and answer date.
    created_date = Column(DateTime(True), server_default=func.now())
    # Update question or answer date.
    updated_date = Column(
        DateTime(True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        server_default=func.now()
    )

    query: sql.select
