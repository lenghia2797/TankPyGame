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
        self.health = 100
        self.damage = 20
        
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.heathBar = GameObject(self.scene, 0, 0, 80, 18, self.scene.game.loader.health_bar, 4)
        
        self.scene.add(self.heathBar)

        self.lastTimeShoot = pygame.time.get_ticks()
        self.timeShoot = 1000
        
        self.bullets = []
        
        self.createBullets()

    def update(self):
        super().update()
        if self.active:
            self.heathBar.x = self.x
            self.heathBar.y = self.y + Constants.TANK_HEIGHT + 2
            self.heathBar.cropX = 82 * self.health / 100
            self.heathBar.cropY = 82
            
    def dead(self):
        self.active = False
        self.visible = False
        self.heathBar.active = False
        self.heathBar.visible = False

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
        if self.type == TankType.PLAYER_1:
            self.scene.play_sound(self.scene.shoot_sound)
        
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
