from camunda.external_task.external_task import ExternalTask, TaskResult
from datetime import datetime
import json
import requests

class BetragUeberweisen:
    def __init__(self):
        self.topic = "betragUeberweisen"

    def func(self, task: ExternalTask) -> TaskResult:
        employee_id = task.get_variable("employee_id")
        description = task.get_variable("description")
        cost = task.get_variable("cost")

        expense_report = {
            "employee_id": employee_id,
            "date": datetime.today().strftime("%d.%m.%Y"),
            "sum": cost,
            "description": description
        }

        url_reports = "http://localhost:3000/expense_reports"
        url_accounts = f"http://localhost:3000/accounts/{employee_id}"

        data = requests.get(url=url_accounts)
        if data.status_code > 300:
            #TODO Logging
            return task.failure()
        
        account = data.json()
        account[0]["balance"] += int(cost)
        account = json.dumps(account).encode('utf8')
        data = requests.put(url=url_accounts, data=account)
        if data.status_code > 300:
            #TODO Logging
            return task.failure()

        data = requests.post(url=url_reports, data=json.dumps(expense_report))
        if data.status_code > 300:
            #TODO Logging
            return task.failure()
        
        return task.complete()
