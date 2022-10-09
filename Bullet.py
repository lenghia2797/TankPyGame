from Constants import Constants
from Enum import TankState
from GameObject import GameObject

class Bullet(GameObject):
    def __init__(self, scene, x, y, width, height, image, depth):
        super().__init__(scene, x, y, width, height, image, depth)
        self.speed = 3
        self.vx = 0
        self.xy = 0
        self.collide = 0
    
    def update(self):
        super().update()
        if self.active:
            self.x += self.vx
            self.y += self.vy
        self.checkPosition()
    
    def checkPosition(self):
        if self.x < 0:
            self.vx *= -1
            self.collide += 1
        if self.y < 0:
            self.vy *= -1
            self.collide += 1
        if self.x + Constants.BULLET_HEIGHT > Constants.SCREEN_WIDTH:
            self.vx *= -1
            self.collide += 1
        if self.y + Constants.BULLET_HEIGHT > Constants.SCREEN_HEIGHT:
            self.vy *= -1
            self.collide += 1
            
        if self.collide >= 2:
            self.active = False