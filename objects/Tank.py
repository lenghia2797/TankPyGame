import math
import pygame
from Constants import Constants
from Enum import TankState, TankType
from gamecore.GameObject import GameObject
from objects.Bullet import Bullet


class Tank(GameObject):
    def __init__(self, scene, x, y, width, height, image, depth, type):
        super().__init__(scene, x, y, width, height, image, depth)
        self.states = [TankState.NORMAL]
        self.type = type

        self.speed = 2
        self.angle = 0
        self.image = pygame.transform.rotate(self.image, self.angle)

        self.lastTimeShoot = pygame.time.get_ticks()
        self.timeShoot = 1000
        
        self.bullets = []
        
        self.createBullets()

    def update(self):
        super().update()

    def setAngle(self, angle):
        self.angle = angle
        self.angle = self.angle % 360
        
    def createBullets(self):
        if self.type == TankType.ENEMY_1:
            image = self.scene.game.loader.bullet_blue_image
        else:
            image = self.scene.game.loader.bullet_red_image
        for i in range(5):
            bullet = Bullet(self.scene, -100, -100, Constants.BULLET_WIDTH,
                            Constants.BULLET_HEIGHT, image, 2)
            bullet.active = False
            bullet.tank = self
            bullet.type = self.type
            self.scene.add(bullet)
            self.bullets.append(bullet)
            
    def shootBullet(self):
        bullet = self.getDeadBullet()
        if not bullet: return
        if not bullet.tank: return
        now = pygame.time.get_ticks()
        
        if now - bullet.tank.lastTimeShoot > bullet.tank.timeShoot:
            bullet.tank.lastTimeShoot = now
            self.shoot(bullet)
            
    def shoot(self, bullet):
        bullet.active = True
        bullet.visible = True
        
        # bullet.collide = 0

        bullet.x = bullet.tank.x + Constants.TANK_WIDTH/2
        bullet.y = bullet.tank.y + Constants.TANK_HEIGHT/2
        bullet.vx = bullet.speed * \
            math.sin((bullet.tank.angle - 180) * math.pi / 180)
        bullet.vy = bullet.speed * \
            math.cos((bullet.tank.angle - 180) * math.pi / 180)
    
    def getDeadBullet(self):
        for bullet in self.bullets:
            if not bullet.active:
                return bullet
        return None
