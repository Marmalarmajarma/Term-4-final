from GameFrame import RoomObject
import pygame
from GameFrame.Globals import Globals

class dificulty_button(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("dificulty selection screen.png")
        self.set_image(image, 1000, 750)
        

        self.handle_key_events = True
        
    
    def key_pressed(self, key):

        if key[pygame.k_1]:
            Globals.dificulty = 1
            self.room.running = False

        if key[pygame.K_2]:
            Globals.dificulty = 2
            self.room.running = False
            
            if key[pygame.k_3]:
                Globals.dificulty = 3
                self.room.running = False