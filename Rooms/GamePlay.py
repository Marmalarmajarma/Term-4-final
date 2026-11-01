from GameFrame import Level
from Objects.Player import Player

class GamePlay(Level):

    def __init__(self, screen, joystics):
        Level.__init__(self, screen, joystics)

        self.set_background_image("Background.png")

        self.add_room_object(Player(self, 0, 0))