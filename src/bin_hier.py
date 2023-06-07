from camunda.external_task.external_task import ExternalTask, TaskResult

class binHier:
    def __init__(self):
        self.topic = "binHier"

    def func(self, task: ExternalTask) -> TaskResult:
        print("bin hier")
        return task.complete()
