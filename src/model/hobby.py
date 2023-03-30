import marshmallow as marsh
from peewee import TextField

from model.base_model import BaseModel


class Hobby(BaseModel):
    class Schema(BaseModel.Schema):
        name = marsh.fields.String(required=True)

        def _make(self, data: dict) -> 'Hobby':
            return Hobby(**data)

    name = TextField(null=False)
