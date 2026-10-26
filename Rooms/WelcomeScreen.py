from GameFrame import Level
from Objects.start_button import Title

class WelcomeScreen(Level):

    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image("Background.png")

        self.add_room_object(Title(self, 0, 0))