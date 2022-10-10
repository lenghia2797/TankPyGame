
import math
from xml.etree.ElementInclude import include
import pygame
from Bullet import Bullet
from Constants import Constants
from Enum import TankState, TankType
from GameObject import GameObject
from Loader import Loader
from Tank import Tank


class Enemy(Tank):
    def __init__(self, scene, x, y, width, height, image, depth):
        super().__init__(scene, x, y, width, height, image, depth)
        self.speedY = 2
        self.rawY = y
        self.moveDown = True
        self.lastTimeShoot = pygame.time.get_ticks()
        self.timeShoot = 500

    def update(self):
        super().update()
        self.autoMove()
        self.updateShoot()

    def updateShoot(self):
        now = pygame.time.get_ticks()
        if now > self.lastTimeShoot + self.timeShoot:
            self.lastTimeShoot = now
            self.shootBullet()

    def updateByState(self):
        for state in self.states:
            if state == TankState.ROTATE_LEFT:
                self.setAngle(self.angle + 1)
                self.image = self.rot_center(self.scene.loader.tank_red_image,
                                             self.angle)
            if state == TankState.ROTATE_RIGHT:
                self.setAngle(self.angle - 1)
                self.image = self.rot_center(self.scene.loader.tank_red_image,
                                             self.angle)
            if state == TankState.UP:
                self.y += self.speed * math.cos(self.angle * math.pi / 180)
                self.x += self.speed * math.sin(self.angle * math.pi / 180)
            if state == TankState.DOWN:
                self.y -= self.speed * math.cos(self.angle * math.pi / 180)
                self.x -= self.speed * math.sin(self.angle * math.pi / 180)

    def autoMove(self):
        if self.moveDown:
            self.y += self.speed
            if self.y > self.rawY + 250:
                self.moveDown = False
        else:
            self.y -= self.speed
            if self.y < self.rawY:
                self.moveDown = True

    def shootBullet(self):
        bullet = self.scene.getBlueDeadBullet()
        if bullet:
            bullet.active = True
            bullet.visible = True
            bullet.collide = 0
            bullet.tank = self
            bullet.x = bullet.tank.x + Constants.TANK_WIDTH/2
            bullet.y = bullet.tank.y + Constants.TANK_HEIGHT/2
            bullet.vx = bullet.speed * \
                math.sin((bullet.tank.angle - 180) * math.pi / 180)
            bullet.vy = bullet.speed * \
                math.cos((bullet.tank.angle - 180) * math.pi / 180)
