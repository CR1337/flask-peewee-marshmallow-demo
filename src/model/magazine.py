import marshmallow as marsh
from peewee import IntegerField

from model.readable import Readable


class Magazine(Readable):

    class Schema(Readable.Schema):
        issue = marsh.fields.Integer()

        def _make(self, data: dict) -> 'Magazine':
            return Magazine(**data)

    issue = IntegerField()
