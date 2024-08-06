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
