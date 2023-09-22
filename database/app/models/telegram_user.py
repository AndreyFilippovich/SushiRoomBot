from sqlalchemy import Column, String, Integer

from app.core.db import Base


class TelegramUser(Base):
    name = Column(String(), nullable=False)
    tg_id = Column(Integer(), nullable=False)
    phone_number = Column(String(), nullable=False)
    birth_day = Column(String(), nullable=False)
