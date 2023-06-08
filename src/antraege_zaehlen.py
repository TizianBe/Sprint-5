from camunda.external_task.external_task import ExternalTask, TaskResult
import requests

class AntraegeZaehlen:
    def __init__(self):
        self.topic = "antraegeZaehlen"

    def func(self, task: ExternalTask) -> TaskResult:
        employee_id = task.get_variable("employee_id")
        url = f"http://localhost:3000/expense_reports?employee_id={employee_id}"

        data = requests.get(url=url)
        reports = data.json()
        if data.status_code > 300:
            #TODO Logging
            return task.failure()
    
        return task.complete({"anzahl_antraege": len(reports)})