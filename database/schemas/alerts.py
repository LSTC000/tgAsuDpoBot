from database.database_setup import BaseModel

from sqlalchemy import Column, BigInteger, sql, DateTime, func


class Alerts(BaseModel):
    __tablename__ = 'alerts'

    # Telegram user id.
    user_id = Column(BigInteger, nullable=False, primary_key=True)
    # Created review date.
    created_date = Column(DateTime(True), server_default=func.now())

    query: sql.select
