from sqlalchemy import Column, String, Integer

from app.core.db import Base


class Promotion(Base):
    text = Column(String(), nullable=False)
