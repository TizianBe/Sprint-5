from camunda.external_task.external_task import ExternalTask, TaskResult

class AntragAbgelehnt:
    def __init__(self):
        self.topic = "antragAbgelehnt"

    def func(self, task: ExternalTask) -> TaskResult:
        name = task.get_variable("employee_name")
        surname = task.get_variable("employee_surname")
        employee_id = task.get_variable("employee_id")
        description = task.get_variable("description")
        cost = task.get_variable("cost")
        print(f"Der Antrag von {name} {surname} (ID: {employee_id}) über {cost} Euro für '{description}' wurde abgelehnt")
        return task.complete()
