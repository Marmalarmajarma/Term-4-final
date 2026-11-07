from GameFrame import RoomObject
import pygame


class Controlls(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("controlls.png")
        self.set_image(image, 1300, 750)
        self.set_timer(40, self.end_room)

    def end_room(self):
        self.room.running = False