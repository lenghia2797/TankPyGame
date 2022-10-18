import math
import pygame
from Constants import Constants
from Enum import TankState, TankType
from gamecore.GameObject import GameObject


class Tank(GameObject):
    def __init__(self, scene, x, y, width, height, image, depth):
        super().__init__(scene, x, y, width, height, image, depth)
        self.states = [TankState.NORMAL]

        self.speed = 1
        self.angle = 0
        self.image = pygame.transform.rotate(self.image, self.angle)

        self.lastTimeShoot = pygame.time.get_ticks()
        self.timeShoot = 200

    def update(self):
        super().update()

    def setAngle(self, angle):
        self.angle = angle
        self.angle = self.angle % 360
