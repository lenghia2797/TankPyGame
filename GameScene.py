import math
import random
import pygame
from Bullet import Bullet
from Constants import Constants
from Enemy import Enemy
from Enum import TankType
from gamecore.Game import Game
from gamecore.GameObject import GameObject
from Player import Player
from Player2 import Player2
from gamecore.Scene import Scene
from ScoreLabel import ScoreLabel, ScoreLabel2
from Tank import Tank
from Wall import Wall
from gamecore.SceneManager import SceneManager


def onClickPlayer():
    print(random.random())


class GameScene(Scene):
    def __init__(self, screen, game: Game, sceneManager: SceneManager):
        super().__init__(screen, game, sceneManager)
        self.name = Constants.GAME_SCENE
        self.gameMode = 2

        self.redBullets = []
        self.blueBullets = []

        self.background = GameObject(self, 0, 0, Constants.SCREEN_WIDTH,
                                     Constants.SCREEN_HEIGHT, self.game.loader.background_image, 0)
        self.player_1_1 = Player(self, 100, 100, Constants.TANK_WIDTH,
                                 Constants.TANK_HEIGHT, self.game.loader.tank_red_image, 3)
        self.player_1_2 = Player(self, 100, 300, Constants.TANK_WIDTH,
                                 Constants.TANK_HEIGHT, self.game.loader.tank_red_image, 3)
        self.player_1_2.type = TankType.AI_1
        self.player_1_2.triangle.visible = False

        if self.gameMode == 2:
            self.player_2_1 = Player2(self, 800, 100, Constants.TANK_WIDTH,
                                      Constants.TANK_HEIGHT, self.game.loader.tank_blue_image, 3)
            self.player_2_2 = Player2(self, 800, 300, Constants.TANK_WIDTH,
                                      Constants.TANK_HEIGHT, self.game.loader.tank_blue_image, 3)
            self.player_2_2.type = TankType.AI_2
            self.player_2_2.triangle.visible = False
        else:

            self.enemy = Enemy(self, 700, 100, Constants.TANK_WIDTH, Constants.TANK_HEIGHT,
                               self.game.loader.tank_blue_image, 3)
            self.enemy.setAngle(90)
            self.enemy.image = self.enemy.rot_center(self.game.loader.tank_blue_image,
                                                     self.enemy.angle)
            self.enemy.type = TankType.ENEMY_1

        self.wall = Wall(self, 400, 400, Constants.WALL_WIDTH,
                         Constants.WALL_HEIGHT, self.game.loader.wall_image, 3)
        for i in range(10):
            bullet = Bullet(self, -100, -100, Constants.BULLET_WIDTH,
                            Constants.BULLET_HEIGHT, self.game.loader.bullet_red_image, 2)
            bullet.active = False
            bullet.tank = self.player_1_1
            bullet.color = 1
            self.add(bullet)
            self.redBullets.append(bullet)

        for i in range(10):
            bullet = Bullet(self, -100, -100, Constants.BULLET_WIDTH,
                            Constants.BULLET_HEIGHT, self.game.loader.bullet_blue_image, 2)
            bullet.active = False
            bullet.color = 2
            if self.gameMode == 2:
                bullet.tank = self.player_2_1
            else:
                bullet.tank = self.enemy
            self.add(bullet)
            self.blueBullets.append(bullet)

        self.add(self.background)
        self.add(self.player_1_1)
        self.add(self.player_1_2)
        self.add(self.player_1_1.triangle)
        self.add(self.player_1_2.triangle)
        self.add(self.wall)
        if self.gameMode == 2:
            self.add(self.player_2_1)
            self.add(self.player_2_2)
            self.add(self.player_2_1.triangle)
            self.add(self.player_2_2.triangle)
        else:
            self.add(self.enemy)

        self.scoreLabel = ScoreLabel(self)
        self.scoreLabel2 = ScoreLabel2(self)

    def update(self):
        running = super().update()
        self.checkCollisionBulletWall(self.redBullets)
        self.checkCollisionBulletWall(self.blueBullets)
        if self.gameMode == 2:
            self.checkCollisionBulletTank(self.redBullets, self.player_2_1)
            self.checkCollisionBulletTank(self.redBullets, self.player_2_2)
        else:
            self.checkCollisionBulletTank(self.redBullets, self.enemy)
        self.checkCollisionBulletTank(self.blueBullets, self.player_1_1)
        self.checkCollisionBulletTank(self.blueBullets, self.player_1_2)

        self.scoreLabel.update()
        self.scoreLabel2.update()

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
                    bullet.collide += 1
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
                    if bullet.color == 1 and (tank.type == TankType.ENEMY_1 or tank.type == TankType.PLAYER_2 or tank.type == TankType.AI_2):
                        ScoreLabel.score += 1
                    if bullet.color == 2 and (tank.type == TankType.PLAYER_1 or tank.type == TankType.AI_1):
                        ScoreLabel2.score += 1

    def shootBullet(self):
        bullet = self.getRedDeadBullet()
        if bullet:
            if self.player_1_1.type == TankType.PLAYER_1:
                bullet.tank = self.player_1_1
            elif self.player_1_1.type == TankType.AI_1:
                bullet.tank = self.player_1_2

            now = pygame.time.get_ticks()
            if now - bullet.tank.lastTimeShoot > bullet.tank.timeShoot:
                bullet.tank.lastTimeShoot = now
                self.shoot(bullet)

    def shootBullet2(self):
        bullet = self.getBlueDeadBullet()
        if bullet:
            if self.gameMode == 2:
                if self.player_2_1.type == TankType.PLAYER_2:
                    bullet.tank = self.player_2_1
                elif self.player_2_1.type == TankType.AI_2:
                    bullet.tank = self.player_2_2

            now = pygame.time.get_ticks()
            if now - bullet.tank.lastTimeShoot > bullet.tank.timeShoot:
                bullet.tank.lastTimeShoot = now
                self.shoot(bullet)

    def shoot(self, bullet):
        bullet.active = True
        bullet.visible = True
        bullet.collide = 0

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
