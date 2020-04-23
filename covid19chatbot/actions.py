# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
class ActionCovidState(Action):

    def name(self) -> Text:
         return "action_covid19_st"

    def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

       output = requests.get("https://api.covid19india.org/data.json").json()
       entities = tracker.latest_message['entities']
       #print("messages", entities)
       state = None

       for i in entities:
            if i['entity'] == "state":
                state = i['value']
       msg=""
       for st in output["statewise"]:
           if st["state"] == state.title():
               print(st)
               msg = "Active :"  +st['active']  +"   Confirmed :" +st['confirmed']  +"  Recovered :"  +st['recovered'] +"   Lastupdate :" +st['lastupdatedtime']

       dispatcher.utter_message(msg)
       return []
