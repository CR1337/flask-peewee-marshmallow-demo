import marshmallow as marsh
from peewee import (ForeignKeyField, IntegerField, Model, SqliteDatabase,
                    TextField)


# Create database instance
db = SqliteDatabase("db.sqlite3")


# All models (classes that need persistance) have to inherit from BaseModel
class BaseModel(Model):
    class Meta:
        database = db  # set the database

    # deserialization using marshmallow
    @classmethod
    def from_dict(cls, data: dict) -> 'BaseModel':
        return cls.Schema().load(data)

    # serialization using marshmallow
    def to_dict(self) -> dict:
        return self.Schema().dump(self)


class Author(BaseModel):
    # These fields are turned into database columns
    name = TextField(null=False)
    age = IntegerField()
    # This field is not persistant
    gangname: str

    # Definition of the marshmallow schema that determines which fields are
    # serialized and deserialized.
    class Schema(marsh.Schema):
        id = marsh.fields.Integer()
        name = marsh.fields.String(required=True)
        age = marsh.fields.Integer(required=True)
        gangname = marsh.fields.String()

        # This defines how json data is turned into an Author object
        @marsh.post_load
        def make_author(self, data, **_):
            return Author(**data)

    # If you want to customize the initialization of a model instance you
    # have to be careful with the following things:
    #
    # 1. You have to call the super().__init__ method with the **kwargs
    # 2. __init__ should only take keyword arguments, hence the ´*´
    # 3. additional arguments need a default value or marshmallow will fail
    def __init__(self, *,  gangname: str = "", **kwargs):
        super().__init__(**kwargs)
        self.gangname = gangname

    def __repr__(self):
        return f"{self.id=!r}, {self.gangname=!r}, {self.name=!r}, {self.age=!r}"


class Readable(BaseModel):
    title = TextField(null=False)
    author = ForeignKeyField(Author, backref='readables')

    class Schema(marsh.Schema):
        id = marsh.fields.Integer()
        title = marsh.fields.String(required=True)
        author = marsh.fields.Nested(Author.Schema, required=True)

        @marsh.post_load
        def make_readable(self, data, **_):
            return Readable(**data)

    def __repr__(self):
        return f"{self.id=!r}, {self.title=!r}, {self.author=!r}"


# You can also inherit from an existing model
class Book(Readable):
    page_count = IntegerField()

    # The marshmallow schema of an inherited model can also be inherited from
    # it's parent's schema
    class Schema(Readable.Schema):
        page_count = marsh.fields.Integer(required=True)

        @marsh.post_load
        def make_book(self, data, **_):
            return Book(**data)

    def __repr__(self):
        return f"{self.id=!r}, {self.title=!r}, {self.author=!r}, {self.page_count=!r}"


class Magazine(Readable):
    issue = IntegerField()

    class Schema(Readable.Schema):
        issue = marsh.fields.Integer(required=True)

        @marsh.post_load
        def make_magazine(self, data, **_):
            return Magazine(**data)

    def __repr__(self):
        return f"{self.id=!r}, {self.title=!r}, {self.author=!r}, {self.issue=!r}"


# This creates the tables in the database if they don't exist yet
with db:
    db.create_tables([Author, Readable, Book, Magazine])
