from GameFrame import RoomObject
import pygame
from GameFrame.Globals import Globals

class play(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("Game play background.png")
        self.set_image(image, 10000, 10000)

        self.top_edge = self.y
        self.bottom_edge = self.y + self.height
        self.left_edge = self.x
        self.right_edge = self.x + self.width


    def step(self):
        self.top_edge = self.y
        self.bottom_edge = self.y + self.height
        self.left_edge = self.x
        self.right_edge = self.x + self.width
        self.out_bounds()    
        self.momentum_update()
    

    def momentum_update(self):
        self.x_speed = Globals.Player_x_speed // 2
        self.y_speed = Globals.Player_y_speed // 2

    def out_bounds(self):
        if Globals.no_mods == False:
            if self.left_edge >= Globals.Player_x_mid:
                Globals.Player_x_speed *= -.5
                Globals.no_mods = True
                self.set_timer(10, self.reset_momentum)

            if self.top_edge >= Globals.Player_y_mid:
                Globals.Player_y_speed *= -.5
                Globals.no_mods = True
                self.set_timer(10, self.reset_momentum)

            if self.right_edge <= Globals.Player_x_mid + 140:
                Globals.Player_x_speed *= -.5
                Globals.no_mods = True
                self.set_timer(10, self.reset_momentum)

            if self.bottom_edge <= Globals.Player_y_mid + 140:
                Globals.Player_x_speed *= -.5
                Globals.no_mods = True
                self.set_timer(10, self.reset_momentum)

    def reset_momentum(self):
        Globals.no_mods = False