from camunda.external_task.external_task import ExternalTask, TaskResult
import json
import requests

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

        data = requests.post(url=url, data=json.dumps(account), headers=headers)
        if data.status_code > 300:
            #TODO Logging
            return task.failure()
    
        return task.complete()
