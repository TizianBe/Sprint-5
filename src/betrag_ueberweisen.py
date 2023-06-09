from camunda.external_task.external_task import ExternalTask, TaskResult
from datetime import datetime
from etc.db import DbConnector
from etc.const import GET, POST, PUT
import json

class BetragUeberweisen:
    def __init__(self):
        self.topic = "betragUeberweisen"

    def func(self, task: ExternalTask) -> TaskResult:
        employee_id = task.get_variable("employee_id")
        description = task.get_variable("description")
        cost = task.get_variable("cost")
        db_connector = DbConnector()

        expense_report = {
            "employee_id": int(employee_id),
            "date": datetime.today().strftime("%d.%m.%Y"),
            "sum": cost,
            "description": description
        }

        url_reports = "http://localhost:3000/expense_reports/"
        url_get_account = f"http://localhost:3000/accounts?employee_id={employee_id}"
        headers = {"Content-Type": "application/json"}

        result = db_connector.access_db(url=url_get_account, type=GET, task=task)
        if type(result) is TaskResult:
            return result
        
        account = result.json()[0]
        account["balance"] += int(cost)
        url_put_account = f"http://localhost:3000/accounts/{account['id']}"
        result = db_connector.access_db(url=url_put_account, type=PUT, task=task, data=json.dumps(account), headers=headers)
        if type(result) is TaskResult:
            return result

        result = db_connector.access_db(url=url_reports, type=POST, task=task, data=json.dumps(expense_report), headers=headers)
        if type(result) is TaskResult:
            return result
        
        return task.complete()