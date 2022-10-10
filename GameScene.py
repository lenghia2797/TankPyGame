import math
import random
import pygame
from Bullet import Bullet
from Constants import Constants
from GameObject import GameObject
from Player import Player
from Scene import Scene
from Tank import Tank

def onClickPlayer():
    print(random.random())

class GameScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.bullets = []
        
        self.background = GameObject(self, 0, 0, Constants.SCREEN_WIDTH, 
                                     Constants.SCREEN_HEIGHT, self.loader.background_image, 0)
        self.player = Player(self, 100, 100, Constants.TANK_WIDTH, 
                             Constants.TANK_HEIGHT, self.loader.tank_red_image, 3)
        for i in range(100):
            bullet = Bullet(self, -100, -100, Constants.BULLET_WIDTH, 
                        Constants.BULLET_HEIGHT, self.loader.bullet_red_image, 2)
            bullet.active = False
            bullet.tank = self.player
            self.add(bullet)
            self.bullets.append(bullet)
        self.player.setKey('down_a', self.player.onPressA)
        self.player.setKey('down_d', self.player.onPressD)
        self.player.setKey('down_w', self.player.onPressW)
        self.player.setKey('down_s', self.player.onPressS)
        self.player.setKey('down_x', self.shootBullet)
        self.player.setKey('up_a', self.player.onReleaseA)
        self.player.setKey('up_d', self.player.onReleaseD)
        self.player.setKey('up_w', self.player.onReleaseW)
        self.player.setKey('up_s', self.player.onReleaseS)
        
        self.add(self.background)
        self.add(self.player)
        
        
    def update(self):
        running = super().update()
        
        return running
    
    def shootBullet(self):
        bullet = self.getDeadBullet()
        if bullet:
            bullet.active = True
            bullet.visible = True
            bullet.collide = 0
            bullet.x = bullet.tank.x + Constants.TANK_WIDTH/2
            bullet.y = bullet.tank.y + Constants.TANK_HEIGHT/2
            bullet.vx = bullet.speed * math.sin((bullet.tank.angle - 180) * math.pi / 180)
            bullet.vy = bullet.speed * math.cos((bullet.tank.angle - 180) * math.pi / 180)
        
    def getDeadBullet(self):
        for bullet in self.bullets:
            if not bullet.active:
                return bullet
        return None
    
    