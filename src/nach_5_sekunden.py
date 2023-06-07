from camunda.external_task.external_task import ExternalTask, TaskResult

class Nach5Sekunden:
    def __init__(self):
        self.topic = "nach5Sekunden"

    def func(self, task: ExternalTask) -> TaskResult:
        print("5 Sekunden")
        return task.complete()