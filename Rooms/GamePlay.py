from GameFrame import Level
from Objects.Player import Player
from Objects.play import play
from Objects.enemy import enemy

class GamePlay(Level):

    def __init__(self, screen, joystics):
        Level.__init__(self, screen, joystics)

        self.set_background_image("Background.png")

        self.add_room_object(Player(self, 0, 0))
        self.add_room_object(enemy(self, 100, 100))

        self.add_room_object(play(self, 0, 0))