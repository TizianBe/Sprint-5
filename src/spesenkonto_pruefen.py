from camunda.external_task.external_task import ExternalTask, TaskResult
import requests

class SpesenkontoPruefen:
    def __init__(self):
        self.topic = "spesenkontoPruefen"

    def func(self, task: ExternalTask) -> TaskResult:
        employee_id = task.get_variable("employee_id")
        account_exists = False
        url = "http://localhost:3000/accounts"
        
        data = requests.get(url=url)
        accounts = data.json()
        if data.status_code > 300:
            #TODO Logging
            return task.failure()
        
        for account in accounts:
            if account.employee_id == employee_id:
                account_exists = True
                break
    
        return task.complete({"konto_exisitiert": account_exists})
