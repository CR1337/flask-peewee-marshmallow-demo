import marshmallow as marsh
from peewee import ForeignKeyField, TextField

from model.author import Author
from model.base_model import BaseModel


class Readable(BaseModel):

    class Schema(BaseModel.Schema):
        title = marsh.fields.String(required=True)
        author_id = marsh.fields.String(required=True)

    title = TextField(null=False)
    author_id = ForeignKeyField(Author, null=False)