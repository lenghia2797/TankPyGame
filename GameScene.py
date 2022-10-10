import math
import random
import pygame
from Bullet import Bullet
from Constants import Constants
from Enum import TankType
from GameObject import GameObject
from Player import Player
from Scene import Scene
from Tank import Tank
from Wall import Wall

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
        self.player2 = Player(self, 100, 300, Constants.TANK_WIDTH, 
                             Constants.TANK_HEIGHT, self.loader.tank_red_image, 3)
        self.player2.type = TankType.AI_1
        self.player2.triangle.visible = False
        
        self.wall = Wall(self, 400, 400, Constants.WALL_WIDTH,
                         Constants.WALL_HEIGHT, self.loader.wall_image, 3)
        for i in range(50):
            bullet = Bullet(self, -100, -100, Constants.BULLET_WIDTH, 
                        Constants.BULLET_HEIGHT, self.loader.bullet_red_image, 2)
            bullet.active = False
            bullet.tank = self.player
            self.add(bullet)
            self.bullets.append(bullet)
        
        self.add(self.background)
        self.add(self.player)
        self.add(self.player2)        
        self.add(self.player.triangle)
        self.add(self.player2.triangle)
        self.add(self.wall)
        
    def update(self):
        running = super().update()
        self.checkCollision()
        
        return running
    
    def checkCollision(self):
        collision_tolerance = 10
        for bullet in self.bullets:
            if bullet.visible:
                bullet_rect = bullet.rect
                wall_rect = self.wall.rect
                if bullet_rect.colliderect(wall_rect):
                    if abs(wall_rect.top - bullet_rect.bottom) < collision_tolerance and bullet.vy > 0:
                        bullet.vy *= -1
                    if abs(wall_rect.bottom - bullet_rect.top) < collision_tolerance and bullet.vy < 0:
                        bullet.vy *= -1
                    if abs(wall_rect.right - bullet_rect.left) < collision_tolerance and bullet.vx < 0:
                        bullet.vx *= -1
                    if abs(wall_rect.left - bullet_rect.right) < collision_tolerance and bullet.vy < 0:
                        bullet.vx *= -1
    
    def shootBullet(self):
        bullet = self.getDeadBullet()
        if bullet:
            bullet.active = True
            bullet.visible = True
            bullet.collide = 0
            if self.player.type == TankType.PLAYER_1:
                bullet.tank = self.player
            else:
                bullet.tank = self.player2
            bullet.x = bullet.tank.x + Constants.TANK_WIDTH/2
            bullet.y = bullet.tank.y + Constants.TANK_HEIGHT/2
            bullet.vx = bullet.speed * math.sin((bullet.tank.angle - 180) * math.pi / 180)
            bullet.vy = bullet.speed * math.cos((bullet.tank.angle - 180) * math.pi / 180)
        
    def getDeadBullet(self):
        for bullet in self.bullets:
            if not bullet.active:
                return bullet
        return None
    
    