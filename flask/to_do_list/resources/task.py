from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import TaskModel
from schemas import TaskSchema, TaskUpdateSchema

blp = Blueprint("Tasks", __name__, description="Operations on tasks")


@blp.route("/tasks/<int:task_id>")
class Task(MethodView):
    @blp.response(200, TaskSchema)
    def get(self, task_id):
        task = TaskModel.query.get_or_404(task_id)

        return task

    def delete(self, task_id):
        task = TaskModel.query.get_or_404(task_id)

        db.session.delete(task)
        db.session.commit()

        return {"message": "Task deleted"}

    @blp.arguments(TaskUpdateSchema)
    @blp.response(200, TaskSchema)
    def put(self, task_data, task_id):
        task = TaskModel.query.get(task_id)

        if task:
            task.name = task_data.get("name", task.name)
            task.status = task_data.get("status", task.status)
        else:
            task = TaskModel(id=task_id, **task_data)

        db.session.add(task)
        db.session.commit()

        return task


@blp.route("/tasks")
class TaskList(MethodView):
    @blp.response(200, TaskSchema(many=True))
    def get(self):
        return TaskModel.query.all()

    @blp.arguments(TaskSchema)
    @blp.response(201, TaskSchema)
    def post(self, task_data):
        task = TaskModel(**task_data)

        try:
            db.session.add(task)
            db.session.commit()
        except SQLAlchemyError:
            abort(
                500,
                message="An error occurred while inserting the task."
            )

        return task
