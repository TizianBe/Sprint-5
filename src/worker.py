from camunda.external_task.external_task_worker import ExternalTaskWorker
from nach_15_sekunden import Nach15Sekunden
from nach_30_sekunden import Nach30Sekunden
from threading import Thread

default_config = {
    "maxTasks": 1,
    "lockDuration": 10000,
    "asyncResponseTimeout": 5000,
    "retries": 3,
    "retryTimeout": 5000,
    "sleepSeconds": 30
}

class Worker:
    def __init__(self):
        self.threads: list(Thread) = []
        self.external_tasks: list() = []
        self.worker_counter = 0

    def add_task(self, external_task) -> bool:
      try:
         topic = external_task.topic
         func = external_task.func
         self.external_tasks.append(external_task)
         print(f"Added {external_task.__class__.__name__} to list of external tasks")
         self.start_thread(topic=topic, func=func)
         return True
      except Exception:
         print(Exception.message)
         return False
      
    def start_thread(self, topic, func):
       self.worker_counter += 1
       external_task_worker: ExternalTaskWorker = ExternalTaskWorker(worker_id=str(self.worker_counter))
       thread: Thread = Thread(target=external_task_worker.subscribe, args=(topic, func))
       thread.daemon = True
       self.threads.append(thread)
       thread.start()
       print(f"Started thread for '{topic}'")

def main():
   worker: Worker = Worker()
   worker.add_task(Nach15Sekunden())
   worker.add_task(Nach30Sekunden())
   while True:
      continue

if __name__ == '__main__':
    try:
       main()
    except KeyboardInterrupt:
       print('Exiting application...')
       exit(1)