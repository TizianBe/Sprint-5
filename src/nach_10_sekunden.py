from camunda.external_task.external_task import ExternalTask, TaskResult

class Nach10Sekunden:
    def __init__(self):
        self.topic = "nach10Sekunden"

    def func(self, task: ExternalTask) -> TaskResult:
        print("10 Sekunden")
        return task.complete()
