import math
import random
import pygame
from objects.Bullet import Bullet
from Constants import Constants
from objects.Enemy import Enemy
from Enum import TankType
from gamecore.Game import Game
from gamecore.GameObject import GameObject
from objects.Player import Player
from objects.Player2 import Player2
from gamecore.Scene import Scene
from ScoreLabel import ScoreLabel, ScoreLabel2
from objects.Tank import Tank
from objects.TileMap import TileMap
from objects.Wall import Wall
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

        # self.background = GameObject(self, -200, -200, Constants.SCREEN_WIDTH * 4,
                                    #  Constants.SCREEN_HEIGHT * 4, self.game.loader.background_image, 0)
        self.player = Player(self, 200, 200, Constants.TANK_WIDTH,
                                 Constants.TANK_HEIGHT, self.game.loader.tank_red_image, 3)
        
        # self.player_1_1.ignoreCamera = True
        # self.player_1_1.triangle.ignoreCamera = True
        # self.player_1_2 = Player(self, 100, 300, Constants.TANK_WIDTH,
        #                          Constants.TANK_HEIGHT, self.game.loader.tank_red_image, 3)
        # self.player_1_2.type = TankType.AI_1
        # self.player_1_2.triangle.visible = False

        if self.gameMode == 2:
            pass
            # self.player_2_1 = Player2(self, 800, 100, Constants.TANK_WIDTH,
            #                           Constants.TANK_HEIGHT, self.game.loader.tank_blue_image, 3)
            # self.player_2_2 = Player2(self, 800, 300, Constants.TANK_WIDTH,
            #                           Constants.TANK_HEIGHT, self.game.loader.tank_blue_image, 3)
            # self.player_2_2.type = TankType.AI_2
            # self.player_2_2.triangle.visible = False
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
            bullet.tank = self.player
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

        # self.add(self.background)
        self.add(self.player)
        # self.add(self.player_1_2)
        self.add(self.player.triangle)
        # self.add(self.player_1_2.triangle)
        # self.add(self.wall)
        if self.gameMode == 2:
            pass
            # self.add(self.player_2_1)
            # self.add(self.player_2_2)
            # self.add(self.player_2_1.triangle)
            # self.add(self.player_2_2.triangle)
        else:
            self.add(self.enemy)

        self.scoreLabel = ScoreLabel(self)
        self.scoreLabel2 = ScoreLabel2(self)
        
        self.map = TileMap(self, 'assets/levelMap.csv')

    def update(self):
        self.screen.fill((243, 199, 79))
        self.updateCameraOffsetObject(
            Constants.SCREEN_WIDTH/2 - self.player.x, 
            Constants.SCREEN_HEIGHT/2 - self.player.y
        )
        running = super().update()
        
        self.checkCollisionPlayerMap()
        
        self.checkCollisionBulletMap(self.redBullets)
        
        # self.checkCollisionBulletWall(self.redBullets)
        # self.checkCollisionBulletWall(self.blueBullets)
        # if self.gameMode == 2:
        #     self.checkCollisionBulletTank(self.redBullets, self.player_2_1)
        #     self.checkCollisionBulletTank(self.redBullets, self.player_2_2)
        # else:
        #     self.checkCollisionBulletTank(self.redBullets, self.enemy)
        # self.checkCollisionBulletTank(self.blueBullets, self.player)
        # self.checkCollisionBulletTank(self.blueBullets, self.player_1_2)

        self.scoreLabel.update()
        self.scoreLabel2.update()

        return running
    
    def checkCollisionPlayerMap(self):
        for tile in self.map.tiles:
            self.checkCollisionPlayerWall(tile)
    
    def checkCollisionPlayerWall(self, wall):
        collision_tolerance = 5
        if not wall.visible: return
        wall_rect = pygame.Rect(wall.x, wall.y,
                                        wall.width, wall.height)
        player_rect = pygame.Rect(self.player.x, self.player.y,
                                          self.player.width, self.player.height)
        if player_rect.colliderect(wall_rect):
            if abs(wall_rect.top - player_rect.bottom) < collision_tolerance :
                # right
                print('right')
                self.player.canMoveRight = False
            elif abs(wall_rect.bottom - player_rect.top) < collision_tolerance :
                # top
                print('top')
                self.player.canMoveUp = False
            elif abs(wall_rect.right - player_rect.left) < collision_tolerance :
                # left
                print('left')
                self.player.canMoveLeft = False
            elif abs(wall_rect.left - player_rect.right) < collision_tolerance :
                # down
                print('down')
                self.player.canMoveDown = False

    def checkCollisionBulletMap(self, bullets):
        for tile in self.map.tiles:
            for bullet in bullets:
                self.checkCollisionBulletWall(bullet, tile)
       
    def checkCollisionBulletWall(self, bullet, wall):
        collision_tolerance = 10
        if not bullet.visible: return
        if not wall.visible: return
        bullet_rect = pygame.Rect(bullet.x, bullet.y,
                                    bullet.width, bullet.height)
        wall_rect = pygame.Rect(wall.x, wall.y,
                                wall.width, wall.height)
        if bullet_rect.colliderect(wall_rect):
            bullet.active = False
            bullet.visible = False
            
    def checkCollisionBulletWall2(self, bullets):
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
            if self.player.type == TankType.PLAYER_1:
                bullet.tank = self.player
            elif self.player.type == TankType.AI_1:
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
