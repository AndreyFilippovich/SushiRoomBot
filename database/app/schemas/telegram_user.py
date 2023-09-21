from pydantic import BaseModel


class TelegramUserCreate(BaseModel):
    name: str
    tg_id: int
    phone_number: str
    birth_day: str
