from camunda.external_task.external_task import ExternalTask, TaskResult

class AntragInBearbeitung:
    def __init__(self):
        self.topic = "antragInBearbeitung"

    def func(self, task: ExternalTask) -> TaskResult:
        name = task.get_variable("name")
        surname = task.get_variable("surname")
        employee_id = task.get_variable("employee_id")
        description = task.get_variable("description")
        cost = task.get_variable("cost")
        print(f"Der Antrag von {name} {surname} (ID: {employee_id}) über {cost} Euro für '{description}' ist noch in Bearbeitung")
        return task.complete()
