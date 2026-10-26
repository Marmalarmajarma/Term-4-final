from GameFrame import Level

class DificultySelection(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.load_image("dificulty selection screen.png")