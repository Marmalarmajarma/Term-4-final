from GameFrame import Level
from Objects.Controlls import Controlls

class controlls(Level):
    
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image("Background.png")
        self.add_room_object(Controlls(self, 0, 0))

        