from camunda.external_task.external_task import ExternalTask, TaskResult
class Nach30Sekunden:
    def __init__(self):
        self.topic = "nach30Sekunden"

    def func(self, task: ExternalTask) -> TaskResult:
        print("30 Sekunden")
        return task.complete()
