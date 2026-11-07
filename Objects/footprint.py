from GameFrame import RoomObject
import random

from GameFrame.Globals import Globals

class footprints(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("footprint.png")
        self.set_image(image, 650, 350)
        self.depth = 3
        facatora = random.randint(600, 850)
        self.set_timer(facatora, self.be_gone)


    def step(self):
        self.momentum_update()

    def momentum_update(self):
        self.x_speed = Globals.Player_x_speed // 2
        self.y_speed = Globals.Player_y_speed // 2

    def be_gone(self):
        self.room.delete_object(self)