from camunda.external_task.external_task import ExternalTask, TaskResult
from etc.db import DbConnector
from etc.const import GET

class MitarbeiterPruefen:
    def __init__(self):
        self.topic = "mitarbeiterPruefen"

    def func(self, task: ExternalTask) -> TaskResult:
        employee_id = task.get_variable("employee_id")
        name = task.get_variable("name")
        surname = task.get_variable("surname")
        employee_exists = False
        url = f"http://localhost:3000/employees/{employee_id}"
        db_connector = DbConnector()
        

        result = db_connector.access_db(url=url, type=GET, task=task)
        if type(result) is TaskResult:
            return result        
        employee = result.json()

        if employee["prename"] == name and employee["surname"] == surname:
            employee_exists = True
    
        return task.complete({"mitarbeiter_exisitiert": employee_exists})
