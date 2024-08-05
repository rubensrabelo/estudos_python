from flask import Blueprint, render_template

from models.task import TaskModel

main = Blueprint("main", __name__)


@main.route("/")
def home():
    tasks = TaskModel.query.all() # Construção de uma pasta serviços para enviar essa função
    return render_template("home.html", tasks=tasks)
