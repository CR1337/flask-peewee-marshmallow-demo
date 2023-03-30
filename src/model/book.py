import marshmallow as marsh
from peewee import IntegerField

from model.readable import Readable


class Book(Readable):

    class Schema(Readable.Schema):
        page_count = marsh.fields.Integer()

        def _make(self, data: dict) -> 'Book':
            return Book(**data)

    page_count = IntegerField()
