from flask import Blueprint, render_template

from services.task_service import TaskService


taskRoute = Blueprint("taskRoute", __name__)


@taskRoute.route("/tasks")
def home():
    tasks = TaskService.get_all_task()

    return render_template("/tasks/home.html", tasks=tasks)
