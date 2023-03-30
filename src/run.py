from typing import Iterator, Type

from app import app
from model.base_model import BaseModel, db


def model_classes() -> Iterator[Type[BaseModel]]:
    def recursive_subclasses(cls: Type) -> Iterator[Type]:
        for subclass in cls.__subclasses__():
            yield from recursive_subclasses(subclass)
            yield subclass
    for subclass in recursive_subclasses(BaseModel):
        yield subclass

if __name__ == "__main__":
    port = 5000
    db.create_tables(model_classes())
    app.run("0.0.0.0", port, debug=True)
