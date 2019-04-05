from rasa_core_sdk import Action
from rasa_core.events import SlotSet
import requests
import json

class ActionJoke(Action):
    def name(self):
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)
        joke = request['value']
        dispatcher.utter_message(joke) 
        return []
