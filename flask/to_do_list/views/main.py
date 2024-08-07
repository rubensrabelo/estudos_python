from flask import Blueprint, render_template

from services.task_service import TaskService


main = Blueprint("main", __name__)


@main.route("/")
def home():
    tasks = TaskService.get_all_task()

    return render_template("home.html", tasks=tasks)
