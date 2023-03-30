from uuid import uuid4
from abc import abstractmethod

import marshmallow as marsh
from peewee import Model, SqliteDatabase, UUIDField

db = SqliteDatabase("db.sqlite3")


class BaseModel(Model):
    class Meta:
        database: SqliteDatabase = db

    class Schema(marsh.Schema):
        id = marsh.fields.String()

        @abstractmethod
        def _make(self, data: dict) -> 'BaseModel':
            raise NotImplementedError()

        @marsh.post_load
        def make(self, data: dict, **_) -> 'BaseModel':
            return self._make(data)

    id = UUIDField(primary_key=True, default=uuid4)

    @classmethod
    def from_dict(cls, data: dict) -> 'BaseModel':
        return cls.Schema().load(data)

    def to_dict(self) -> dict:
        return self.Schema().dump(self)
