from camunda.external_task.external_task import ExternalTask, TaskResult

class Nach7Tagen:
    def __init__(self):
        self.topic = "nach7Tagen"

    def func(self, task: ExternalTask) -> TaskResult:
        x = task.get_extension_properties()
        print(x)
        return task.complete()
