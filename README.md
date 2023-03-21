# flask-peewee-marshmallow-demo

## Description
This demo shows the interaction of flask, peewee and marshmallow. It implements a simple model with `Authors` and `Readables` and `Books` and `Magazines` that inherit from `Readable`. There is a rudamentary frontend that lets you send requests to an Flask-API providing methods to create, show and delete elements. Marshmallow is used to serialize and deserialize objects. The ORM-model as well as the (de)serialization is defined in `src/model.py` and explained with comments. The API is defined in `src/app.py`.

## Usage
Run `poetry run python3 src/run.py`. The frontend will automatically open in your browser.
