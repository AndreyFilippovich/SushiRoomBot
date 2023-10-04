from sqlalchemy import Column, String, Integer, BigInteger

from app.core.db import Base


class TelegramUser(Base):
    name = Column(String(), nullable=False)
    tg_id = Column(BigInteger(), nullable=False)
    phone_number = Column(String(), nullable=False)
    birth_day = Column(String(), nullable=False)
