from flask import Blueprint, render_template

blp = Blueprint("createBook", __name__)


@blp.route("/books/create")
def create_book():
    return render_template("/books/createbook.html")
