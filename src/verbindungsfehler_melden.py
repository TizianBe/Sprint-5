from camunda.external_task.external_task import ExternalTask, TaskResult

class VerbindungsfehlerMelden:
    def __init__(self):
        self.topic = "verbindungsfehlerMelden"

    def func(self, task: ExternalTask) -> TaskResult:
        print("Verbindung zum Datenbank-Server ist fehlgeschlagen")
        return task.complete()