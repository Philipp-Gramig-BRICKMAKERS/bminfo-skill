from mycroft import MycroftSkill, intent_file_handler


class Bminfo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('bark.intent')
    def handle_bark(self, message):
        self.speak_dialog('bark')


def create_skill():
    return Bminfo()
