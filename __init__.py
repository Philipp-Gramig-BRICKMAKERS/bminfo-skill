from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from datetime import datetime


class Bminfo(MycroftSkill):
    def __init__(self):
        super(Bminfo, self).__init__(name="Bminfo")

    def getAllRooms(self):
    
    def getTodaysRoomsEvents(self, allRooms):

    @intent_handler(IntentBuilder("").require("Room"))
    def handle_room_intent(self, message):
        allRooms = self.getAllRooms()
        allEvents = self.getTodaysRoomsEvents(allRooms)

        for event in allEvents:
            self.log.info(event)
            self.speak_dialog("room.is.free.after", data={'room': "Huddle Room", 'end': "12:30"})

def create_skill():
    return Bminfo()
