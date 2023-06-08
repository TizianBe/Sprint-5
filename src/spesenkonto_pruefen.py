from camunda.external_task.external_task import ExternalTask, TaskResult

class SpesenkontoPruefen:
    def __init__(self):
        self.topic = "spesenkontoPruefen"

    def func(self, task: ExternalTask) -> TaskResult:
        url = "http://localhost:3000/"
        
        task.complete()
