from mycroft import MycroftSkill, intent_file_handler


class FoundingFather(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('father.founding.intent')
    def handle_father_founding(self, message):
        self.speak_dialog('father.founding')


def create_skill():
    return FoundingFather()

