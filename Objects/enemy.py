from GameFrame import RoomObject
import pygame 
from GameFrame.Globals import Globals

class enemy(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("enemy.png")
        self.set_image(image, 140, 140)
        self.register_collision_object("Player")
        self.depth = 1
        

    def step(self):
        self.momentum_update()

    def momentum_update(self):
    
        self.x_speed = Globals.Player_x_speed // 2
        self.y_speed = Globals.Player_y_speed // 2

    def handle_collision(self, other, other_type):
        if other_type == "Player":
            if Globals.no_mods == False:
                Globals.Player_x_speed *= -3
                Globals.Player_y_speed *= -3
                Globals.LIVES -= 1
                Globals.no_mods = True
                self.set_timer(10, self.reset_momentum)

    def reset_momentum(self):
        Globals.no_mods = False