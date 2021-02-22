from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

class TestSkill(MycroftSkill):


    def __init__(self):
        super(TestSkill, self).__init__(name="TestSkill")

    @intent_handler(IntentBuilder("").require("Room"))
    def handle_room_intent(self, message):
        self.speak_dialog("room.is.free")

def create_skill():
    return TestSkill()
