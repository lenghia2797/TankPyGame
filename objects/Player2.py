
import math
from xml.etree.ElementInclude import include
import pygame
from objects.Bullet import Bullet
from Constants import Constants
from Enum import TankState, TankType
from gamecore.GameObject import GameObject
from gamecore.Loader import Loader
from objects.Tank import Tank


class Player2(Tank):
    def __init__(self, scene, x, y, width, height, image, depth):
        super().__init__(scene, x, y, width, height, image, depth)
        self.type = TankType.PLAYER_2
        self.setKey('down_left', self.onPressLeft)
        self.setKey('down_right', self.onPressRight)
        self.setKey('down_down', self.onPressDown)
        self.setKey('down_up', self.onPressUp)
        self.setKey('down_enter', self.scene.shootBullet2)
        self.setKey('down_o', self.switchPlayer)
        self.setKey('up_left', self.onReleaseLeft)
        self.setKey('up_right', self.onReleaseRight)
        self.setKey('up_down', self.onReleaseDown)
        self.setKey('up_up', self.onReleaseUp)

        self.triangle = GameObject(self.scene, self.x + Constants.TANK_WIDTH / 2,
                                   self.y, Constants.TRIANGLE_WIDTH - 5,
                                   Constants.TRIANGLE_HEIGHT, self.scene.game.loader.triangle_image, 4)

    def update(self):
        super().update()
        if self.type == TankType.PLAYER_2:
            self.updateByState()
        elif self.type == TankType.AI_2:
            self.autoMove()

        self.triangle.x = self.x + Constants.TANK_WIDTH / 2
        self.triangle.y = self.y - 5

    def switchPlayer(self):
        if (self.type == TankType.PLAYER_2):
            self.type = TankType.AI_2
            self.triangle.visible = False
        elif (self.type == TankType.AI_2):
            self.type = TankType.PLAYER_2
            self.triangle.visible = True

    def updateByState(self):
        for state in self.states:
            if state == TankState.ROTATE_LEFT:
                self.setAngle(self.angle + 1)
                self.image = self.rot_center(self.scene.game.loader.tank_blue_image,
                                             self.angle)
            if state == TankState.ROTATE_RIGHT:
                self.setAngle(self.angle - 1)
                self.image = self.rot_center(self.scene.game.loader.tank_blue_image,
                                             self.angle)
            if state == TankState.DOWN:
                self.y += self.speed * math.cos(self.angle * math.pi / 180)
                self.x += self.speed * math.sin(self.angle * math.pi / 180)
            if state == TankState.UP:
                self.y -= self.speed * math.cos(self.angle * math.pi / 180)
                self.x -= self.speed * math.sin(self.angle * math.pi / 180)

    def onReleaseLeft(self):
        self.states.remove(TankState.ROTATE_LEFT)

    def onReleaseRight(self):
        self.states.remove(TankState.ROTATE_RIGHT)

    def onReleaseUp(self):
        self.states.remove(TankState.UP)

    def onReleaseDown(self):
        self.states.remove(TankState.DOWN)

    def onPressLeft(self):
        self.states.append(TankState.ROTATE_LEFT)

    def onPressRight(self):
        self.states.append(TankState.ROTATE_RIGHT)

    def onPressUp(self):
        self.states.append(TankState.UP)

    def onPressDown(self):
        self.states.append(TankState.DOWN)

    def autoMove(self):
        pass
