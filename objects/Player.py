
import math
from xml.etree.ElementInclude import include
import pygame
from objects.Bullet import Bullet
from Constants import Constants
from Enum import TankState, TankType
from gamecore.GameObject import GameObject
from gamecore.Loader import Loader
from objects.Tank import Tank


class Player(Tank):
    def __init__(self, scene, x, y, width, height, image, depth):
        super().__init__(scene, x, y, width, height, image, depth, TankType.PLAYER_1)
        self.canMoveLeft = True
        self.canMoveRight = True
        self.canMoveUp = True
        self.canMoveDown = True
        self.setKey('down_a', self.onPressA)
        self.setKey('down_d', self.onPressD)
        self.setKey('down_w', self.onPressW)
        self.setKey('down_s', self.onPressS)
        self.setKey('down_x', self.shootBullet)
        self.setKey('down_q', self.switchPlayer)
        self.setKey('up_a', self.onReleaseA)
        self.setKey('up_d', self.onReleaseD)
        self.setKey('up_w', self.onReleaseW)
        self.setKey('up_s', self.onReleaseS)

        self.triangle = GameObject(self.scene, self.x + Constants.TANK_WIDTH / 2,
                                   self.y, Constants.TRIANGLE_WIDTH - 5,
                                   Constants.TRIANGLE_HEIGHT, self.scene.game.loader.triangle_image, 4)

    def update(self):
        super().update()
        if self.type == TankType.PLAYER_1:
            self.updateByState()
        elif self.type == TankType.AI_1:
            self.autoMove()

        self.triangle.x = self.x + Constants.TANK_WIDTH / 2
        self.triangle.y = self.y - 5

    def switchPlayer(self):
        if (self.type == TankType.PLAYER_1):
            self.type = TankType.AI_1
            self.triangle.visible = False
        elif (self.type == TankType.AI_1):
            self.type = TankType.PLAYER_1
            self.triangle.visible = True

    def updateByState(self):
        dx = 0
        dy = 0
        for state in self.states:
            if state == TankState.ROTATE_LEFT:
                self.setAngle(self.angle + 1)
                self.image = self.rot_center(self.scene.game.loader.tank_red_image,
                                             self.angle)
            if state == TankState.ROTATE_RIGHT:
                self.setAngle(self.angle - 1)
                self.image = self.rot_center(self.scene.game.loader.tank_red_image,
                                             self.angle)
            if state == TankState.DOWN:
                dy = self.speed * math.cos(self.angle * math.pi / 180)
                dx = self.speed * math.sin(self.angle * math.pi / 180)
                if dy < 0 and not self.canMoveUp: return
                if dy > 0 and not self.canMoveDown: return
                if dx < 0 and not self.canMoveLeft: return
                if dx > 0 and not self.canMoveRight: return
                self.y += dy
                self.x += dx
            if state == TankState.UP:
                dy = - self.speed * math.cos(self.angle * math.pi / 180)
                dx = - self.speed * math.sin(self.angle * math.pi / 180)
                if dy < 0 and not self.canMoveUp: return
                if dy > 0 and not self.canMoveDown: return
                if dx < 0 and not self.canMoveLeft: return
                if dx > 0 and not self.canMoveRight: return
                self.y += dy
                self.x += dx
        if dy > 0:
            self.canMoveUp = True
        if dy < 0:
            self.canMoveDown = True
        if dx < 0:
            self.canMoveRight = True
        if dx > 0:
            self.canMoveLeft = True

    def onReleaseA(self):
        self.states.remove(TankState.ROTATE_LEFT)

    def onReleaseD(self):
        self.states.remove(TankState.ROTATE_RIGHT)

    def onReleaseW(self):
        self.states.remove(TankState.UP)

    def onReleaseS(self):
        self.states.remove(TankState.DOWN)

    def onPressA(self):
        self.states.append(TankState.ROTATE_LEFT)

    def onPressD(self):
        self.states.append(TankState.ROTATE_RIGHT)

    def onPressW(self):
        self.states.append(TankState.UP)

    def onPressS(self):
        self.states.append(TankState.DOWN)

    def autoMove(self):
        pass
