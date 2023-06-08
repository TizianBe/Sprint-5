from camunda.external_task.external_task import ExternalTask, TaskResult
import requests

class SpesenkontoPruefen:
    def __init__(self):
        self.topic = "spesenkontoPruefen"

    def func(self, task: ExternalTask) -> TaskResult:
        employee_id = task.get_variable("employee_id")
        account_exists = False
        url = f"http://localhost:3000/accounts?employee_id={employee_id}"
        
        data = requests.get(url=url)
        accounts = data.json()
        if data.status_code > 300:
            #TODO Logging
            return task.failure()
        
        if len(accounts) > 0:
            account_exists = True
    
        return task.complete({"konto_exisitiert": account_exists})
