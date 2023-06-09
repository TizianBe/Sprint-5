from camunda.external_task.external_task import ExternalTask, TaskResult
from etc.db import DbConnector
from etc.const import GET

class MitarbeiterPruefen:
    def __init__(self):
        self.topic = "mitarbeiterPruefen"

    def func(self, task: ExternalTask) -> TaskResult:
        employee_id = task.get_variable("employee_id")
        name = task.get_variable("employee_name")
        surname = task.get_variable("employee_surname")
        employee_exists = False
        url = f"http://localhost:3000/employees/{employee_id}"
        db_connector = DbConnector()
        

        result = db_connector.access_db(url=url, type=GET, task=task)
        if type(result) is TaskResult:
            return result        
        employee = result.json()

        if employee["prename"].lower() == name.lower() and employee["surname"].lower() == surname.lower():
            employee_exists = True
    
        return task.complete({"mitarbeiter_exisitiert": employee_exists})
