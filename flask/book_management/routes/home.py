from flask import Blueprint, render_template

blp = Blueprint("home", __name__)


@blp.route("/")
def home():
    return render_template("home.html")
