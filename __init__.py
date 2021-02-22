from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

class RoomSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder("").require("Room"))
    def handle_room_intent(self, message):
        self.speak_dialog("room.is.free")

def create_skill():
    return RoomSkill()
