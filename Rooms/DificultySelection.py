from GameFrame import Level
from Objects.dificulty_button import dificulty_button

class DificultySelection(Level):
    
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image("Background.png")

        self.add_room_object(dificulty_button(self, 150, 0))