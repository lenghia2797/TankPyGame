import math
import random
import pygame
from Bullet import Bullet
from Constants import Constants
from Enemy import Enemy
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
        self.redBullets = []
        self.blueBullets = []

        self.background = GameObject(self, 0, 0, Constants.SCREEN_WIDTH,
                                     Constants.SCREEN_HEIGHT, self.loader.background_image, 0)
        self.player = Player(self, 100, 100, Constants.TANK_WIDTH,
                             Constants.TANK_HEIGHT, self.loader.tank_red_image, 3)
        self.player2 = Player(self, 100, 300, Constants.TANK_WIDTH,
                              Constants.TANK_HEIGHT, self.loader.tank_red_image, 3)
        self.player2.type = TankType.AI_1
        self.player2.triangle.visible = False

        self.enemy = Enemy(self, 700, 100, Constants.TANK_WIDTH, Constants.TANK_HEIGHT,
                           self.loader.tank_blue_image, 3)
        self.enemy.setAngle(90)
        self.enemy.image = self.enemy.rot_center(self.loader.tank_blue_image,
                                                 self.enemy.angle)
        self.enemy.type = TankType.ENEMY_1

        self.wall = Wall(self, 400, 400, Constants.WALL_WIDTH,
                         Constants.WALL_HEIGHT, self.loader.wall_image, 3)
        for i in range(10):
            bullet = Bullet(self, -100, -100, Constants.BULLET_WIDTH,
                            Constants.BULLET_HEIGHT, self.loader.bullet_red_image, 2)
            bullet.active = False
            bullet.tank = self.player
            self.add(bullet)
            self.redBullets.append(bullet)

        for i in range(10):
            bullet = Bullet(self, -100, -100, Constants.BULLET_WIDTH,
                            Constants.BULLET_HEIGHT, self.loader.bullet_blue_image, 2)
            bullet.active = False
            bullet.tank = self.enemy
            self.add(bullet)
            self.blueBullets.append(bullet)

        self.add(self.background)
        self.add(self.player)
        self.add(self.player2)
        self.add(self.player.triangle)
        self.add(self.player2.triangle)
        self.add(self.wall)
        self.add(self.enemy)

    def update(self):
        running = super().update()
        self.checkCollisionBulletWall(self.redBullets)
        self.checkCollisionBulletWall(self.blueBullets)
        self.checkCollisionBulletTank(self.redBullets, self.enemy)
        self.checkCollisionBulletTank(self.blueBullets, self.player)
        self.checkCollisionBulletTank(self.blueBullets, self.player2)

        return running

    def checkCollisionBulletWall(self, bullets):
        collision_tolerance = 10
        for bullet in bullets:
            if bullet.visible:
                bullet_rect = pygame.Rect(bullet.x, bullet.y,
                                          bullet.width, bullet.height)
                wall_rect = pygame.Rect(self.wall.x, self.wall.y,
                                        self.wall.width, self.wall.height)
                if bullet_rect.colliderect(wall_rect):
                    if abs(wall_rect.top - bullet_rect.bottom) < collision_tolerance and bullet.vy > 0:
                        bullet.vy *= -1
                    if abs(wall_rect.bottom - bullet_rect.top) < collision_tolerance and bullet.vy < 0:
                        bullet.vy *= -1
                    if abs(wall_rect.right - bullet_rect.left) < collision_tolerance and bullet.vx < 0:
                        bullet.vx *= -1
                    if abs(wall_rect.left - bullet_rect.right) < collision_tolerance and bullet.vy > 0:
                        bullet.vx *= -1

    def checkCollisionBulletTank(self, bullets, tank):
        for bullet in bullets:
            if bullet.visible:
                bullet_rect = pygame.Rect(bullet.x, bullet.y,
                                          bullet.width, bullet.height)
                tank_rect = pygame.Rect(tank.x, tank.y,
                                        tank.width, tank.height)
                if bullet_rect.colliderect(tank_rect):
                    bullet.active = False
                    bullet.visible = False
                    bullet.x = -100
                    print(123)

    def shootBullet(self):
        bullet = self.getRedDeadBullet()
        if bullet:
            bullet.active = True
            bullet.visible = True
            bullet.collide = 0
            if self.player.type == TankType.PLAYER_1:
                bullet.tank = self.player
            elif self.player.type == TankType.AI_1:
                bullet.tank = self.player2
            bullet.x = bullet.tank.x + Constants.TANK_WIDTH/2
            bullet.y = bullet.tank.y + Constants.TANK_HEIGHT/2
            bullet.vx = bullet.speed * \
                math.sin((bullet.tank.angle - 180) * math.pi / 180)
            bullet.vy = bullet.speed * \
                math.cos((bullet.tank.angle - 180) * math.pi / 180)

    def getRedDeadBullet(self):
        for bullet in self.redBullets:
            if not bullet.active:
                return bullet
        return None

    def getBlueDeadBullet(self):
        for bullet in self.blueBullets:
            if not bullet.active:
                return bullet
        return None
