from typing import Any, List

from starlette.requests import Request
from starlette.responses import Response
from starlette.templating import Jinja2Templates
from starlette_admin import CustomView, action
from starlette_admin.contrib.sqla import ModelView
from starlette_admin.exceptions import ActionFailed

from app.core.db import AsyncSessionLocal
from app.crud.sales import get_sale_by_id
from app.crud.telegram_user import get_all_users_ids
from app.services.messaging import mass_send


class TGUserView(ModelView):
    fields = [
        "tg_id",
        "name",
        "phone_number",
        "birth_day",
    ]


class PromotionView(ModelView):
    fields = [
        "text",
    ]

class SalesView(ModelView):
    fields = [
        "text",
    ]


class SalesView(ModelView):
    actions = ["send_all", "delete"]

    @action(
        name="send_all",
        text="Разослать всем",
        confirmation="Вы уверенны что хотите разослать это всем?",
        submit_btn_text="Да, продолжить.",
        submit_btn_class="btn-success",
    )
    async def mass_send(self, request: Request, pks: List[Any]):
        async with AsyncSessionLocal() as session:
            chat_ids = await get_all_users_ids(session)
            for message_id in pks:
                message_db = await get_sale_by_id(int(message_id), session)
                await mass_send(
                    chat_ids,
                    message=message_db.text,
                    link=message_db.link,
                    picture=message_db.picture,
                    file=message_db.file,
                )
        if not pks:
            raise ActionFailed('Извините, данное действие не выполнимо.')