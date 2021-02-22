from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from datetime import datetime


class Bminfo(MycroftSkill):
    def __init__(self):
        super(Bminfo, self).__init__(name="Bminfo")

    def getAllRooms(self):
        return [
            {
                "displayName": "Atari",
                "uid": "2a628728-9927-462e-99d9-0f268034ed97"
            },
            {
                "displayName": "C64",
                "uid": "e500e314-b1e4-44e0-8604-9d8c38b1cea3"
            },
            {
                "displayName": "Huddle-Room",
                "uid": "267b167a-10cc-4317-b76c-1d78902072ba"
            },
            {
                "displayName": "PlayStation",
                "uid": "41fd8e85-4629-42cf-b2fa-08a34d36422e"
            },
            {
                "displayName": "Switch",
                "uid": "6a81ff99-d32c-4451-9ea4-0f0c2772a82c"
            },
            {
                "displayName": "Xbox",
                "uid": "d42a2ef1-7cd4-4c48-81b6-39030991d6cc"
            }
        ]
    
    def getTodaysRoomsEvents(self, allRooms):
        return [
            {
                "room": "Huddle Room",
                "subject": "Johannes Büllesbach",
                "start": "10:15",
                "end": "12:30",
                "organizerProfileImage": "/user/johannes.buellesbach@brickmakers.de/picture",
            },
            {
                "room": "Atari",
                "subject": "Johannes Büllesbach",
                "start": "10:15",
                "end": "12:30",
                "organizerProfileImage": "/user/johannes.buellesbach@brickmakers.de/picture",
            }
        ]

    @intent_handler(IntentBuilder("").require("Room"))
    def handle_room_intent(self, message):
        allRooms = self.getAllRooms()
        allEvents = self.getTodaysRoomsEvents(allRooms)

        for event in allEvents:
            self.log.info(event)
            self.log.warning(event.room)
            # self.speak_dialog("room.is.free.after", data={"room": event.room, "end": event.end})

def create_skill():
    return Bminfo()
