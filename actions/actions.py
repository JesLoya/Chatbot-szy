# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
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
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType
from connect_db import search_location,search_order
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
class Searchlocation(Action):
    
    def name(self) -> Text:
        return"action_search_location"

    def run(
        self,
        dispatcher: "CollectingDispatcher", 
        tracker: Tracker, domain: "DomainDict"
        ) -> List[Dict[Text, Any]]:
        location=search_location(tracker.get_slot("city_name"))
        print(location)
        return [SlotSet(key="location",value=location)]

class SearchOrder(Action):
    def name(self) -> Text:
        return"action_return_goods_feedback"

    def run(
        self,
        dispatcher: "CollectingDispatcher", 
        tracker: Tracker, domain: "DomainDict"
        ) -> List[Dict[Text, Any]]:
        time=search_order(tracker.get_slot("order_number"))
        time1 = int(time)
        if 0<time1<4:
            dispatcher.utter_message(text="OK, the return address is xxxxxxxxx")
        elif time1==0:
            dispatcher.utter_message(text="Sorry, the goods have not arrived yet")
        else:
            dispatcher.utter_message(text="Sorry, the goods cannot be returned after three days")
        return [SlotSet(key="order_time",value=time)]
        