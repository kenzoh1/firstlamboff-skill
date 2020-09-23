from mycroft import MycroftSkill, intent_file_handler


class Firstlamboff(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('firstlamboff.intent')
    def handle_firstlamboff(self, message):
        self.speak_dialog('firstlamboff')


def create_skill():
    return Firstlamboff()

