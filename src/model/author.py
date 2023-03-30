import marshmallow as marsh
from peewee import ForeignKeyField, IntegerField, TextField

from model.base_model import BaseModel
from model.hobby import Hobby


class Author(BaseModel):

    class Schema(BaseModel.Schema):
        name = marsh.fields.String(required=True)
        age = marsh.fields.Integer(required=True)
        gangname = marsh.fields.String()

        def _make(self, data: dict) -> 'Author':
            return Author(**data)

    name = TextField(null=False)
    age = IntegerField()

    gangname: str

    def __init__(self, *, gangname: str = "", **kwargs):
        super().__init__(**kwargs)
        self.gangname = gangname


class AuthorXHobby(BaseModel):

    class Schema(BaseModel.Schema):
        hobby_id = marsh.fields.String(required=True)
        author_id = marsh.fields.String(required=True)
        proficiency = marsh.fields.Integer()

        def _make(self, data: dict) -> 'AuthorXHobby':
                return AuthorXHobby(**data)

    hobby_id = ForeignKeyField(Hobby)
    author_id = ForeignKeyField(Author)
    proficiency = IntegerField(default=0)
