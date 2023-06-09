from camunda.external_task.external_task import ExternalTask, TaskResult, Variables
import requests
from etc.const import GET, POST, PUT 

class DbConnector:
    
    def access_db(self, url, type, task: ExternalTask, data=None, headers=None) -> TaskResult | requests.Response:
        result = None
        retry_counter = task.get_variable("retry_counter")
        if retry_counter is None:
            retry_counter = 0
        
        try:
            if type is GET:
                result = requests.get(url=url, headers=headers)
            elif type is POST:
                result = requests.post(url=url, data=data, headers=headers)
            elif type is PUT:
                result = requests.put(url=url, data=data, headers=headers)
            else:
                raise ValueError
            if result.status_code > 300:
                raise requests.exceptions.ConnectionError
            return result
        except requests.exceptions.ConnectionError as err:
            retry_counter += 1
            return task.bpmn_error(error_code="VerbindungFehlgeschlagenError", error_message="Verbindungsversuch fehlgeschlagen", variables={"retry_counter": retry_counter})
        except Exception as err:
            m = f"Ein unerwarteter Fehler ist aufgetreten.\n{repr(err)}"
            return task.bpmn_error(error_code="UnerwarteterFehlerError", error_message=m)
      