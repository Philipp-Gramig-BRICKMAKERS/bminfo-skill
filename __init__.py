from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from datetime import datetime
from .apiService import *


class Bminfo(MycroftSkill):
    def __init__(self):
        super(Bminfo, self).__init__(name="Bminfo")
    
    @intent_handler(IntentBuilder("").require("Room"))
    def handle_room_intent(self, message):
        todayRoomEvents = getTodaysLastRoomEvents()
        for roomEvent in todayRoomEvents:
            if(roomEvent['eventEndTime'] > 0):
                self.speak_dialog("room.is.free.after", data={'room': roomEvent["roomName"], 'end': roomEvent["eventEndTime"]})
            else:
                self.speak_dialog("room.is.free", data={'room': roomEvent["roomName"]})
    
    @intent_handler(IntentBuilder("").require("New").require("Brickmakers"))
    def handle_newBrickmakers_intent(self, message):
        newBrickmakers = getNewBrickmakers()

        if(len(newBrickmakers) > 0):
            for newBrickmaker in newBrickmakers:
                self.speak(newBrickmaker['name'] + ", ")
            self.speak_dialog("new.brickmakers")
        else:
            self.speak_dialog('no.new.brickmakers')

    @intent_handler(IntentBuilder("").require("Event"))
    def handle_event_intent(self, message):
        allEventsThisWeek = getAllCalenderEvents();

        for event in allEventsThisWeek:
            self.speak_dialog("event", data={'subject': event["subject"], 'name': event["name"]})


def create_skill():
    return Bminfo()
