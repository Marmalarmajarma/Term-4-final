from GameFrame import RoomObject
import pygame
from GameFrame.Globals import Globals
from Objects.footprint import footprints
import random


class Player(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.handle_key_events = True
        self.handle_collision = True
        self.depth = 4
        self.t = 0
        image = self.load_image("player.png")
        self.set_image(image, 140, 140)

    def step(self):
        self.update_middle()

        if Globals.Player_x_speed != 0:
            if Globals.sneaking == False:
                self.footprint(10)

        if Globals.Player_y_speed != 0:
            if Globals.sneaking == False:
                self.footprint(10)

        self.momentum_update()

    def update_middle(self):
        self.x_middle = (Globals.SCREEN_WIDTH / 2) - (self.width/ 2)
        self.y_middle = (Globals.SCREEN_HEIGHT / 2) - (self.height/ 2)
        Globals.Player_x_mid = (Globals.SCREEN_WIDTH / 2) - (self.width/ 2)
        Globals.Player_y_mid = (Globals.SCREEN_HEIGHT / 2) - (self.height/ 2)

        self.x = self.x_middle
        self.y = self.y_middle

    def key_pressed(self, key):
        if Globals.no_mods == False:
            if key[pygame.K_d]:
                Globals.Player_x_speed -= 5

            if key[pygame.K_w]:
                Globals.Player_y_speed += 5

            if key[pygame.K_a]:
                Globals.Player_x_speed += 5

            if key[pygame.K_s]:
                Globals.Player_y_speed -= 5

        if key[pygame.K_SPACE]:
            Globals.sneaking = True

        else:
            Globals.sneaking = False

    def momentum_update(self):
        if Globals.Player_x_speed >= 1:
            Globals.Player_x_speed -= 1

        if Globals.Player_x_speed == 0:
            Globals.Player_x_speed = 0

        if Globals.Player_x_speed <= -1:
            Globals.Player_x_speed += 1

        if Globals.Player_y_speed >= 1:
            Globals.Player_y_speed -= 1

        if Globals.Player_y_speed == 0:
            Globals.Player_y_speed = 0

        if Globals.Player_y_speed <= -1:
            Globals.Player_y_speed += 1

        if Globals.Player_x_speed >= 50:
            Globals.Player_x_speed = 50

        if Globals.Player_y_speed >= 50:
            Globals.Player_y_speed = 50

        if Globals.Player_x_speed <= -50:
            Globals.Player_x_speed = -50

        if Globals.Player_y_speed <= -50:
            Globals.Player_y_speed = -50
    
   
    def footprint(self, frame):
        self.t = Globals.t_foot
        
        if self.t >= frame:
            self.room.add_room_object(footprints(self.room, Globals.Player_x_mid - (self.x / 3) - 70, Globals.Player_y_mid - (self.y / 3) + 35))

            Globals.t_foot = 0

        else:
            Globals.t_foot += 1