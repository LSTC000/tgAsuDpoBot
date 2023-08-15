from database.database_setup import BaseModel

from sqlalchemy import Column, BigInteger, sql


class Alerts(BaseModel):
    __tablename__ = 'alerts'

    # Telegram user id.
    user_id = Column(BigInteger, nullable=False, primary_key=True)

    query: sql.select
