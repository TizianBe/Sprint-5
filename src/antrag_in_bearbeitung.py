from camunda.external_task.external_task import ExternalTask, TaskResult

class AntragInBearbeitung:
    def __init__(self):
        self.topic = "antragInBearbeitung"

    def func(self, task: ExternalTask) -> TaskResult:
        print("Antrag ist noch in Bearbeitung")
        return task.complete()
