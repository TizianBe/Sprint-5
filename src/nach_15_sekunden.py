from camunda.external_task.external_task import ExternalTask, TaskResult
# configuration for the Client
# default_config = {
#     "maxTasks": 1,
#     "lockDuration": 10000,
#     "asyncResponseTimeout": 5000,
#     "retries": 3,
#     "retryTimeout": 5000,
#     "sleepSeconds": 30
# }

class Nach15Sekunden:
    def __init__(self):
        self.topic = "nach15Sekunden"

    def func(self, task: ExternalTask) -> TaskResult:
        print("15 Sekunden")
        return task.complete()