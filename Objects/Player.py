from GameFrame import RoomObject
import pygame
from GameFrame.Globals import Globals
import random

class Player(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.handle_key_events = True
        self.handle_collision = True

        self.frame_UP = []
        self.frame_Down = []
        self.frame_Left = []
        self.frame_Right = []

        self.right_frame = 0
        self.left_frame = 0
        self.up_frame = 0
        self.down_frame = 0

        for index in range(0, 4):
            self.frame_UP.append(self.load_image(f"Player/Up/{index}.png"))

        for index in range(0, 4):
            self.frame_Down.append(self.load_image(f"Player/Down/{index}.png"))

        for index in range(0, 4):
            self.frame_Left.append(self.load_image(f"Player/Left/{index}.png"))

        for index in range(0, 4):
            self.frame_Right.append(self.load_image(f"Player/Right/{index}.png"))

        self.set_image(self.frame_Right[0], 100, 140)

    def step(self):
        self.update_middle()
        self.update_animation()
        
    def update_middle(self):
        self.x_middle = (Globals.SCREEN_WIDTH/ 2) - (self.width/ 2)
        self.y_middle = (Globals.SCREEN_HEIGHT / 2) - (self.height/ 2)

        self.x = self.x_middle
        self.y = self.y_middle

    def update_animation(self):
        if Globals.Player_x_speed > 0:
            self.update_Right()

        elif Globals.Player_x_speed < 0:
            self.update_Left()

        if Globals.Player_y_speed > 0:
            self.update_Down()

        elif Globals.Player_y_speed < 0:
            self.update_Up()

    def update_Right(self):
        self.left_frame = 0
        self.up_frame = 0
        self.down_frame = 0

        if self.right_frame == 3:
            self.set_image(self.frame_Right[3])
            self.right_frame = 0
        
        self.set_image(self.frame_Right[self.right_frame])
        self.right_frame += 1

    def update_Left(self):
        self.right_frame = 0
        self.up_frame = 0
        self.down_frame = 0

        if self.left_frame == 3:
            self.set_image(self.frame_Left[3])
            self.left_frame = 0
        
        self.set_image(self.frame_Right[self.right_frame])
        self.right_frame += 1

    def update_Down(self):
        self.left_frame = 0
        self.up_frame = 0
        self.right_frame = 0

        if self.down_framee == 3:
            self.set_image(self.frame_Down[3])
            self.down_frame = 0
        
        self.set_image(self.frame_Down[self.down_frame])
        self.down_frame += 1

    def update_Up(self):
        self.left_frame = 0
        self.Right_frame = 0
        self.down_frame = 0

        if self.up_frame == 3:
            self.set_image(self.frame_Up[3])
            self.up_frame = 0
        
        self.set_image(self.frame_Up[self.up_frame])
        self.up_frame += 1