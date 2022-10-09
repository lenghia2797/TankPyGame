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
                             Constants.TANK_HEIGHT, self.loader.tank_yellow_image, 3)
        for i in range(20):
            bullet = Bullet(self, -100, -100, Constants.BULLET_WIDTH, 
                        Constants.BULLET_HEIGHT, self.loader.bullet_blue_image, 2)
            bullet.active = False
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
        bullet.active = True
        bullet.x = self.player.x
        bullet.y = self.player.y
        bullet.vx = -4
        bullet.vy = -4
        
    def getDeadBullet(self):
        for bullet in self.bullets:
            if not bullet.active:
                return bullet
    
    