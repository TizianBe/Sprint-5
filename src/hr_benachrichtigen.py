from camunda.external_task.external_task import ExternalTask, TaskResult

class HrBenachrichtigen:
    def __init__(self):
        self.topic = "hrBenachrichtigen"

    def func(self, task: ExternalTask) -> TaskResult:
        name = task.get_variable("employee_name")
        surname = task.get_variable("employee_surname")
        employee_id = task.get_variable("employee_id")
        print(f"Es wurde ein Antrag für den Mitarbeiter {name} {surname} (ID: {employee_id}) eingereicht. Der Mitarbeiter existiert so aber in der DB nicht.")
        return task.complete()