from camunda.external_task.external_task import ExternalTask, TaskResult
from etc.db import DbConnector
from etc.const import GET

class AntraegeZaehlen:
    def __init__(self):
        self.topic = "antraegeZaehlen"

    def func(self, task: ExternalTask) -> TaskResult:
        employee_id = task.get_variable("employee_id")
        url = f"http://localhost:3000/expense_reports?employee_id={employee_id}"
        db_connector = DbConnector()

        result = db_connector.access_db(url=url, type=GET, task=task)
        if type(result) is TaskResult:
            return result
        reports = result.json()
    
        return task.complete({"anzahl_antraege": len(reports)})