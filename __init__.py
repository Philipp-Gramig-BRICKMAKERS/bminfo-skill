from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG


class Bminfo(MycroftSkill):
    def __init__(self):
        super(Bminfo, self).__init__(name="Bminfo")

    @intent_handler(IntentBuilder("").require("Room"))
    def handle_room_intent(self, message):
        self.speak_dialog("room.is.free")

def create_skill():
    return Bminfo()
