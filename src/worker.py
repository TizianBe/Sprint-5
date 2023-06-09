from camunda.external_task.external_task_worker import ExternalTaskWorker
from nach_7_tagen import Nach7Tagen
from spesenkonto_pruefen import SpesenkontoPruefen
from spesenkonto_anlegen import SpesenkontoAnlegen
from antraege_zaehlen import AntraegeZaehlen
from betrag_ueberweisen import BetragUeberweisen
from antrag_abgebrochen import AntragAbgebrochen
from antrag_in_bearbeitung import AntragInBearbeitung
from antrag_abgelehnt import AntragAbgelehnt
from verbindungsfehler_melden import VerbindungsfehlerMelden
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
         self.start_thread(topic=topic, func=func)
         print(f"Started worker for external task '{topic}'")
         return True
      except Exception as err:
         print(err.message)
         return False
      
    def start_thread(self, topic, func):
       self.worker_counter += 1
       external_task_worker: ExternalTaskWorker = ExternalTaskWorker(worker_id=str(self.worker_counter), config=default_config)
       thread: Thread = Thread(target=external_task_worker.subscribe, args=(topic, func))
       thread.daemon = True
       self.threads.append(thread)
       thread.start()

    def await_death(self):
       while True:
          continue

def main():
   worker: Worker = Worker()

   tasks: list() = [
      Nach7Tagen(),
      SpesenkontoPruefen(),
      SpesenkontoAnlegen(),
      AntraegeZaehlen(),
      BetragUeberweisen(),
      AntragAbgebrochen(),
      AntragAbgelehnt(),
      AntragInBearbeitung(),
      VerbindungsfehlerMelden()
   ]

   for task in tasks:
      worker.add_task(task)

   worker.await_death()

if __name__ == '__main__':
    try:
       main()
    except KeyboardInterrupt:
       print('Exiting application...')
       exit(1)