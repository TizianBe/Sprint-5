from camunda.external_task.external_task import ExternalTask, TaskResult
from datetime import datetime
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
        annual_count = 0
        for report in reports:
            report_year = datetime.strptime(report["date"], "%d.%m.%Y").strftime("%Y")
            current_year = datetime.today().strftime("%Y")
            if report_year == current_year:
                annual_count += 1
    
        return task.complete({"anzahl_antraege": annual_count})