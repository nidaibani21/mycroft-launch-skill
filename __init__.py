from mycroft import MycroftSkill, intent_file_handler


class MycroftLaunch(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('launch.mycroft.intent')
    def handle_launch_mycroft(self, message):
        self.speak_dialog('launch.mycroft')


def create_skill():
    return MycroftLaunch()

