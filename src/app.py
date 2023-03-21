from flask import Flask, render_template, request

from model import Author, Book, Magazine, Readable

app = Flask(__name__)


@app.route("/", methods=['GET'])
def route_root():
    return render_template("index.html"), 200


@app.route("/authors", methods=['GET', 'POST'])
def route_authors():
    if request.method == 'GET':
        return [a.to_dict() for a in Author.select()], 200
    elif request.method == 'POST':
        print(request.json)
        Author.from_dict(request.json).save()
        return {}, 200


@app.route("/author/<int:author_id>", methods=['GET', 'DELETE'])
def route_author(author_id: int):
    try:
        author = Author.get(Author.id == author_id)
    except Author.DoesNotExist:
        return {}, 404
    if request.method == 'GET':
        return author.to_dict(), 200
    elif request.method == 'DELETE':
        author.delete_instance()
        return {}, 200


@app.route("/books", methods=['GET', 'POST'])
def route_books():
    if request.method == 'GET':
        return [b.to_dict() for b in Book.select()], 200
    elif request.method == 'POST':
        Book.from_dict(request.json).save()
        return {}, 200


@app.route("/book/<int:book_id>", methods=['GET', 'DELETE'])
def route_book(book_id: int):
    try:
        book = Book.get(Book.id == book_id)
    except Book.DoesNotExist:
        return {}, 404
    if request.method == 'GET':
        return book.to_dict(), 200
    elif request.method == 'DELETE':
        book.delete_instance()
        return {}, 200


@app.route("/magazines", methods=['GET', 'POST'])
def route_magazines():
    if request.method == 'GET':
        return [m.to_dict() for m in Magazine.select()], 200
    elif request.method == 'POST':
        Magazine.from_dict(request.json).save()
        return {}, 200


@app.route("/magazine/<int:magazine_id>", methods=['GET', 'DELETE'])
def route_magazine(magazine_id: int):
    try:
        magazine = Magazine.get(Magazine.id == magazine_id)
    except Magazine.DoesNotExist:
        return {}, 404
    if request.method == 'GET':
        return magazine.to_dict(), 200
    elif request.method == 'DELETE':
        magazine.delete_instance()
        return {}, 200


@app.route("/readables", methods=['GET'])
def route_readables():
    return [r.to_dict() for r in Readable.select()], 200


@app.route("/readable/<int:readable_id>", methods=['GET', 'DELETE'])
def route_readable(readable_id: int):
    try:
        readable = Readable.get(Readable.id == readable_id)
    except Readable.DoesNotExist:
        return {}, 404
    if request.method == 'GET':
        return readable.to_dict(), 200
    elif request.method == 'DELETE':
        readable.delete_instance()
        return {}, 200
