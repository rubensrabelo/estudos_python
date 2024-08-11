from flask import Blueprint, render_template, request, redirect, url_for

from services.task_service import TaskService


taskRoute = Blueprint("taskRoute", __name__)


@taskRoute.route("/tasks", methods=["GET"])
def home():
    tasks = TaskService.get_all_task()

    return render_template("/tasks/home.html", tasks=tasks)


@taskRoute.route("/tasks/create", methods=["GET", "POST"])
def create_task():
    if request.method == "POST":
        task_data = request.form.get("title")
        TaskService.create_task(task_data)
        return redirect(url_for("/tasks"))

    tasks = TaskService.get_all_task()

    return render_template("/tasks/create.html", tasks=tasks)
