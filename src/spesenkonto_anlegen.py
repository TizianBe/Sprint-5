from camunda.external_task.external_task import ExternalTask, TaskResult
from etc.db import DbConnector
from etc.const import POST
import json

class SpesenkontoAnlegen:
    def __init__(self):
        self.topic = "spesenkontoAnlegen"

    def func(self, task: ExternalTask) -> TaskResult:
        employee_id = task.get_variable("employee_id")
        url = "http://localhost:3000/accounts/"
        headers = {"Content-Type": "application/json"}
        account = {
            "employee_id": int(employee_id),
            "balance": 0
        }
        db_connector = DbConnector()

        result = db_connector.access_db(url=url, type=POST, task=task, data=json.dumps(account), headers=headers)
        if type(result) is TaskResult:
            return result
        return task.complete()
