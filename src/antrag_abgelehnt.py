from camunda.external_task.external_task import ExternalTask, TaskResult

class AntragAbgelehnt:
    def __init__(self):
        self.topic = "antragAbgelehnt"

    def func(self, task: ExternalTask) -> TaskResult:
        print("Antrag wurde abgelehnt")
        return task.complete()
