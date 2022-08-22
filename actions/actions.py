# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import json

from typing import Any, Text, Dict, List

from google.auth.transport import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType, ConversationPaused, ConversationResumed, SessionStarted, ActionExecuted
from rasa_sdk.executor import CollectingDispatcher

class ActionService(Action):

     def name(self) -> Text:
         return "action_service"

     def run(self, dispatcher: CollectingDispatcher,
         tracker: Tracker,
         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload":'/Payment{"issue_type":"Payment"}', "title": "എന്റെ പേയ്‌മെന്റ് അപ്‌ഡേറ്റ് ചെയ്‌തിട്ടില്ല"},
             {"payload":'/Bounce{"issue_type":"Bounce"}', "title": "എന്റെ ബൗൺസ് അല്ലെങ്കിൽ പെനൽ ചാർജുകൾ അവലോകനം ചെയ്യുക"},
             {"payload":'/Extra{"issue_type":"Extra"}', "title": "ഞാൻ അധിക Emi അല്ലെങ്കിൽ ചാർജുകൾ നൽകി"},
             {"payload":'/Uninstall{"issue_type":"Uninstall"}', "title": "എനിക്ക് ആപ്ലിക്കേഷൻ അൺഇൻസ്റ്റാൾ ചെയ്യണം"},
             {"payload":'/Locked{"issue_type":"Locked"}', "title": "എന്റെ ഉപകരണം ലോക്ക് ചെയ്‌തിരിക്കുന്നു"},
             {"payload":'/Different{"issue_type":"Different"}', "title": "ഞാൻ മറ്റൊരു പ്രശ്നം നേരിടുന്നു"},
             {"payload": '/Emi{"issue_type":"Emi"}', "title": "Emi പണമടയ്ക്കാൻ കൂടുതൽ സമയം വേണം"},
             {"payload": '/Human{"issue_type":"Human"}', "title": "മനുഷ്യനോട് കൂടുതൽ സംസാരിക്കേണ്ടതുണ്ട്"},

        ]
        dispatcher.utter_message(text="നിങ്ങൾ സഹായം തേടുന്ന വിഷയം തിരഞ്ഞെടുക്കുക", buttons=buttons)


        return []



class CheckLock(Action):

    def name(self) -> Text:
        return "check_lock"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
        dispatcher.utter_message(text= "നിങ്ങൾക്ക് കാലഹരണപ്പെട്ട ഇമി പേയ്‌മെന്റ് ഉണ്ട്. ഫോൺ അൺലോക്ക് ചെയ്യാൻ പണമടയ്ക്കുക")
        return []


class CheckDevicePayment(Action):

    def name(self) -> Text:
        return "check_payment_D"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #for blob in tracker.latest_message['entities']:
        #print(tracker.slots)
        #print(tracker.latest_message)
        message="പുതിയ പേയ്‌മെന്റുകളൊന്നും കണ്ടെത്താനാവുന്നില്ല. പേയ്‌മെന്റ് വിശദാംശങ്ങൾ പങ്കിടുക"
        status="success";
     
        dispatcher.utter_message(text= message)
        return [SlotSet("syncstatus", status)]


class CheckPersonalPayment(Action):

    def name(self) -> Text:
        return "check_payment_P"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text= "പുതിയ പേയ്‌മെന്റുകളൊന്നും കണ്ടെത്താനായില്ല. പേയ്‌മെന്റ് വിശദാംശങ്ങൾ പങ്കിടുക")

        return []


class ValidateDiffForm(Action):

    def name(self) -> Text:
        return "Diff_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict
    ) -> List[EventType]:
                required_slots = ["Diff_title"]

                for slot_name in required_slots:
                    if tracker.slots.get(slot_name) is None:
                        return[SlotSet("requested_slot",slot_name)]

                return[SlotSet("requested_slot",None)]


class ActionSubmit(Action):

    def name(self) -> Text:
        return "action_Diff_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: "DomainDict",
            ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="വിവരങ്ങൾക്ക് നന്ദി. ഞങ്ങളുടെ കസ്റ്റമർ കെയർ എക്സിക്യൂട്ടീവ് ഉടൻ നിങ്ങളെ ബന്ധപ്പെടും")

        return[]


class CheckLoanStatus(Action):

    def name(self) -> Text:
        return "check_loan_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text= "നിങ്ങളുടെ വ്യക്തിഗത വായ്പ ഇതുവരെ പൂർത്തിയായിട്ടില്ല. നിങ്ങൾക്ക് അൺഇൻസ്റ്റാൾ ചെയ്യാൻ കഴിയും അപേക്ഷ പൂർത്തിയാകുമ്പോൾ.")

        return []


class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        # the session should begin with a `session_started` event
        events = [SessionStarted()]

        dispatcher.utter_message(text=" പുതിയ സെഷൻ ആരംഭിച്ചു")

        # any slots that should be carried over should come after the
        # `session_started` event


        # an `action_listen` should be added at the end as a user message follows
        events.append(ActionExecuted("action_listen"))

        return events




class fetch_id(Action):

    def name(self) -> Text:
        return "fetch_id"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        data=1
        return []


class check_bounce_charge(Action):

    def name(self) -> Text:
        return "check_bounce_charge"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text= "  checking ")

        return []


class Notdeducted(Action):

    def name(self) -> Text:
        return "action_Notdeducted"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text= " ഞങ്ങളുടെ രേഖകൾ പ്രകാരം നിങ്ങളുടെ ബാങ്ക് മതിയായ ഫണ്ട് ഇല്ലെന്ന് ചൂണ്ടിക്കാട്ടി നിരസിച്ചു  ")

        return []

class Nachmandate(Action):

    def name(self) -> Text:
        return "action_nachmandate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text= "ഞങ്ങളുടെ രേഖകൾ പ്രകാരം നിങ്ങളുടെ ബാങ്ക് മതിയായ ഫണ്ടുകളില്ലെന്ന് പ്രസ്താവിക്കുകയും നിരസിക്കുകയും ചെയ്തു.നിങ്ങളുടെ ബാങ്കുമായി പേയ്മെന്റ് നില സ്ഥിരീകരിക്കുക.")

        return []




