# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content


class ActionCoffeeList(Action):

    def name(self) -> Text:
        return "action_coffee_list"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text = "Here are the coffee types that we sell :")
        dispatcher.utter_message(text=" - Americano \n - Cappucino \n - Espresso")

        return []

class ActionSendCoffeeEmail(Action):

    def name(self) -> Text:
        return "action_coffee_mail"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        email = tracker.get_slot("email")
        coffee = tracker.get_slot("coffee")

        #SEND EMAIL 
        sg = sendgrid.SendGridAPIClient(api_key='API KEY !') #Free api key from sendgrid.
        from_email = Email("lucien.ledune.ds@gmail.com")  # Change to your verified sender
        to_email = To(email)  # Change to your recipient
        subject = "Your coffee order"
        content = Content("text/plain", "Here's the {} you ordered".format(coffee))
        mail = Mail(from_email, to_email, subject, content)

        # Get a JSON-ready representation of the Mail object
        mail_json = mail.get()

        # Send an HTTP POST request to /mail/send
        response = sg.client.mail.send.post(request_body=mail_json)



        return []


