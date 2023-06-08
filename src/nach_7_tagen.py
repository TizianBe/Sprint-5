from camunda.external_task.external_task import ExternalTask, TaskResult

class Nach7Tagen:
    def __init__(self):
        self.topic = "nach7Tagen"

    def func(self, task: ExternalTask) -> TaskResult:
        name = task.get_variable("employee_name")
        surname = task.get_variable("surname")
        print(f"{name} {surname}")
        return task.complete()
