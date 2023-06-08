from camunda.external_task.external_task import ExternalTask, TaskResult

class AntragAbgebrochen:
    def __init__(self):
        self.topic = "antragAbgebrochen"

    def func(self, task: ExternalTask) -> TaskResult:
        print("Antragsbearbeitung wurde abgebrochen")
        return task.complete()
