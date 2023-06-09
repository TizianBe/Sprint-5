from camunda.external_task.external_task import ExternalTask, TaskResult

class AntragAbgebrochen:
    def __init__(self):
        self.topic = "antragAbgebrochen"

    def func(self, task: ExternalTask) -> TaskResult:
        name = task.get_variable("employee_name")
        surname = task.get_variable("employee_surname")
        employee_id = task.get_variable("employee_id")
        description = task.get_variable("description")
        cost = task.get_variable("cost")
        print(f"Die Bearbeitung des Antrags von {name} {surname} (ID: {employee_id}) über {cost} Euro für '{description}' wurde abgebrochen. Der Antrag müsste nochmals eingereicht werden")
        return task.complete()
