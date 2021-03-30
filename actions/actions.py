# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
# https://github.com/scalableminds/chatroom
# rasa run --credentials ./credentials.yml  --enable-api --auth-token XYZ123 --model ./models --endpoints ./endpoints.yml --cors "*"


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class utterUserInformation(Action):

    def name(self) -> Text:
        return "action_get_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            #db_query = "SELECT * FROM services"
            #db_query_get = getData(db_query)
            #json_string = json.dumps(db_query_get)
            #print(json_string)
            dispatcher.utter_message(text="hello from actions.py")
            return []