import pygame
from Enum import TankState, TankType
from GameObject import GameObject

class Tank(GameObject):
    def __init__(self, scene, x, y, width, height, image, depth):
        super().__init__(scene, x, y, width, height, image, depth)
        self.states = [TankState.NORMAL]
        self.type = TankType.PLAYER_1
        self.speed = 1
        self.angle = 0
        self.image = pygame.transform.rotate(self.image, self.angle)
        
    def update(self):
        super().update()
        
    def setAngle(self, angle):
        self.angle = angle
        self.angle = self.angle % 360