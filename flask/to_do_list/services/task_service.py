from resources.task import TaskList


class TaskService:
    @staticmethod
    def get_all_task():
        service = TaskList()
        response = service.get()

        if response.status_code == 200:
            tasks = response.json
        else:
            tasks = []
        return tasks

    @staticmethod
    def create_task(task_data):
        service = TaskList()
        status_code, response = service.post(task_data)

        if status_code == 201:
            tasks = response.json
        else:
            tasks = []
        return tasks
