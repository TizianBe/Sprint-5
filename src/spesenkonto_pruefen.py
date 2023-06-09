from camunda.external_task.external_task import ExternalTask, TaskResult
from etc.db import DbConnector
from etc.const import GET

class SpesenkontoPruefen:
    def __init__(self):
        self.topic = "spesenkontoPruefen"

    def func(self, task: ExternalTask) -> TaskResult:
        employee_id = task.get_variable("employee_id")
        account_exists = False
        url = f"http://localhost:3000/accounts?employee_id={employee_id}"
        db_connector = DbConnector()
        

        result = db_connector.access_db(url=url, type=GET, task=task)
        if type(result) is TaskResult:
            return result        
        accounts = result.json()

        if len(accounts) > 0:
            account_exists = True
    
        return task.complete({"konto_exisitiert": account_exists})
