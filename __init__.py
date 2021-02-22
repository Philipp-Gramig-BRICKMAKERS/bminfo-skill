from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

class TestSkill(MycroftSkill):


    def __init__(self):
        super(TestSkill, self).__init__(name="TestSkill")

    @intent_handler(IntentBuilder("").require("Room"))
    def handle_room_intent(self, message):
        self.speak_dialog("room.is.free")

    @intent_handler(IntentBuilder("").require("Event").require("Day"))
    def handle_event_intent(self, message):
        if message.data["Day"] == "friday":
            self.speak_dialog("what.event", data={"day": message.data["Day"]})
        else-if message.data["Day"] == "next week":  
            self.speak_dialog("what.event", data={"day": message.data["Day"]})

def create_skill():
    return TestSkill()
