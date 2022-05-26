from abstractions.laser import Laser

class DiagonalLaserLeft(Laser):
    def __init__(self, x, y, img):
        super().__init__(x - 75, y, img)
    def move(self, vel):
        self.y += vel * 3
        self.x -= vel * 3