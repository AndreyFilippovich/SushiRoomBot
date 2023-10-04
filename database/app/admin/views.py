from starlette_admin.contrib.sqla import ModelView


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