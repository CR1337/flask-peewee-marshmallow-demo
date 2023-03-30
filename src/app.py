from flask import Flask, render_template, request

from model.author import Author, AuthorXHobby
from model.book import Book
from model.magazine import Magazine
from model.readable import Readable
from model.hobby import Hobby

app = Flask(__name__)


@app.route("/", methods=['GET'])
def route_root():
    return render_template("index.html"), 200


@app.route("/hobbies", methods=['GET', 'POST'])
def route_hobbies():
    if request.method == 'GET':
        return [h.to_dict() for h in Hobby.select()], 200
    elif request.method == 'POST':
        Hobby.from_dict(request.json).save(force_insert=True)
        return {}, 200


@app.route("/hobby/<hobby_id>", methods=['GET', 'DELETE'])
def route_hobby(hobby_id: str):
    try:
        hobby = Hobby.get(Hobby.id == hobby_id)
    except Hobby.DoesNotExist:
        return {}, 404
    if request.method == 'GET':
        return hobby.to_dict(), 200
    elif request.method == 'DELETE':
        hobby.delete_instance()
        return {}, 200


@app.route("/authors", methods=['GET', 'POST'])
def route_authors():
    if request.method == 'GET':
        return [a.to_dict() for a in Author.select()], 200
    elif request.method == 'POST':
        Author.from_dict(request.json).save(force_insert=True)
        return {}, 200


@app.route("/author/<author_id>", methods=['GET', 'DELETE'])
def route_author(author_id: str):
    try:
        author = Author.get(Author.id == author_id)
    except Author.DoesNotExist:
        return {}, 404
    if request.method == 'GET':
        return author.to_dict(), 200
    elif request.method == 'DELETE':
        author.delete_instance()
        return {}, 200


@app.route("/authors-x-hobbies", methods=['GET', 'POST'])
def route_authors_x_hobbies():
    if request.method == 'GET':
        return [axh.to_dict() for axh in AuthorXHobby.select()], 200
    elif request.method == 'POST':
        AuthorXHobby.from_dict(request.json).save(force_insert=True)
        return {}, 200


@app.route(
    "/author-x-hobby/<author_id>/<hobby_id>",
    methods=['GET', 'DELETE']
)
def route_author_x_hobby(author_id: str, hobby_id: str):
    try:
        author_x_hobby = AuthorXHobby.get(
            (AuthorXHobby.author_id == author_id)
            & (AuthorXHobby.hobby_id == hobby_id)
        )
    except AuthorXHobby.DoesNotExist:
        return {}, 404
    if request.method == 'GET':
        return author_x_hobby.to_dict(), 200
    elif request.method == 'DELETE':
        author_x_hobby.delete_instance()
        return {}, 200


@app.route("/books", methods=['GET', 'POST'])
def route_books():
    if request.method == 'GET':
        return [b.to_dict() for b in Book.select()], 200
    elif request.method == 'POST':
        Book.from_dict(request.json).save(force_insert=True)
        return {}, 200


@app.route("/book/<book_id>", methods=['GET', 'DELETE'])
def route_book(book_id: str):
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
        Magazine.from_dict(request.json).save(force_insert=True)
        return {}, 200


@app.route("/magazine/<magazine_id>", methods=['GET', 'DELETE'])
def route_magazine(magazine_id: str):
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


@app.route("/readable/<readable_id>", methods=['GET', 'DELETE'])
def route_readable(readable_id: str):
    try:
        readable = Readable.get(Readable.id == readable_id)
    except Readable.DoesNotExist:
        return {}, 404
    if request.method == 'GET':
        return readable.to_dict(), 200
    elif request.method == 'DELETE':
        readable.delete_instance()
        return {}, 200
