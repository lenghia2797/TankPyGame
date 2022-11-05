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

from pygame import mixer

def onClickPlayer():
    print(random.random())


class GameScene(Scene):
    def __init__(self, screen, game: Game, sceneManager: SceneManager):
        super().__init__(screen, game, sceneManager)
        self.name = Constants.GAME_SCENE
        
        mixer.init()
        mixer.music.set_volume(0.1)

        # mixer.music.load('assets/sounds/music_background.mp3')
        # mixer.music.play(-1)
        self.load_sound()

        self.run()
    
    def run(self):
        super().run()
        self.bullets = []
        self.player = Player(self, 200, 200, Constants.TANK_WIDTH,
                                 Constants.TANK_HEIGHT, self.game.loader.tank_red_image, 3)
        
        self.bullets += self.player.bullets

        self.wall = Wall(self, 400, 400, Constants.WALL_WIDTH,
                         Constants.WALL_HEIGHT, self.game.loader.wall_image, 3)


        self.add(self.player)
        self.add(self.player.triangle)

        self.scoreLabel = ScoreLabel(self)
        self.scoreLabel2 = ScoreLabel2(self)
        
        self.map = TileMap(self, 'assets/levelMap.csv')
        
        for enemy in self.map.enemies:
            self.bullets += enemy.bullets
    
    def load_sound(self):
        self.shoot_sound = mixer.Sound('assets/sounds/sound_shoot.mp3')
        self.bullet_hit_sound = mixer.Sound('assets/sounds/sound_bullet_hit.mp3')
        self.score_sound = mixer.Sound('assets/sounds/sound_score.mp3')
        # self.power_up_sound = mixer.Sound('assets/sounds/sound_power_up.mp3')
        self.fail_sound = mixer.Sound('assets/sounds/sound_fail.mp3')
            
    def play_sound(self, sound):
        mixer.Sound.play(sound)
        
    def update(self):
        self.screen.fill((243, 199, 79))
        self.updateCameraOffsetObject(
            Constants.SCREEN_WIDTH/2 - self.player.x, 
            Constants.SCREEN_HEIGHT/2 - self.player.y
        )
        running = super().update()
        
        self.checkCollisionPlayerMap()
        
        self.checkCollisionBulletMap()
        
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
        
        for coin in self.map.coins:
            self.checkCollisionPlayerCoin(coin)
            
        for item in self.map.items:
            self.checkCollisionPlayerItem(item)
            
        for bullet in self.bullets:   
            if bullet.type == TankType.ENEMY_1:
                self.checkCollisionPlayerBullet(bullet)
    
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
                self.player.canMoveRight = False
            elif abs(wall_rect.bottom - player_rect.top) < collision_tolerance :
                # top
                self.player.canMoveUp = False
            elif abs(wall_rect.right - player_rect.left) < collision_tolerance :
                # left
                self.player.canMoveLeft = False
            elif abs(wall_rect.left - player_rect.right) < collision_tolerance :
                # down
                self.player.canMoveDown = False

    def checkCollisionBulletMap(self):
        for tile in self.map.tiles:
            for bullet in self.bullets:
                self.checkCollisionBulletWall(bullet, tile)
                
        for enemy in self.map.enemies:
            for bullet in self.bullets:   
                if bullet.type == TankType.PLAYER_1:
                    self.checkCollisionBulletEnemy(bullet, enemy)
       
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
            if bullet.type == TankType.PLAYER_1:
                self.play_sound(self.bullet_hit_sound)
            
    def checkCollisionBulletEnemy(self, bullet, enemy):
        collision_tolerance = 10
        if not bullet.visible: return
        if not enemy.visible: return
        bullet_rect = pygame.Rect(bullet.x, bullet.y,
                                    bullet.width, bullet.height)
        enemy_rect = pygame.Rect(enemy.x, enemy.y,
                                enemy.width, enemy.height)
        if bullet_rect.colliderect(enemy_rect):
            bullet.active = False
            bullet.visible = False
            enemy.health -= bullet.tank.damage
            if enemy.health <= 0:
                enemy.active = False
                enemy.visible = False
                self.play_sound(self.score_sound)
                ScoreLabel.score += 1
                
    def checkCollisionPlayerBullet(self, bullet):
        collision_tolerance = 10
        if not bullet.visible: return
        if not self.player.visible: return
        bullet_rect = pygame.Rect(bullet.x, bullet.y,
                                    bullet.width, bullet.height)
        player_rect = pygame.Rect(self.player.x, self.player.y,
                                self.player.width, self.player.height)
        if bullet_rect.colliderect(player_rect):
            bullet.active = False
            bullet.visible = False
            self.player.health -= bullet.tank.damage
            if self.player.health <= 0:
                self.player.active = False
                self.player.visible = False
                self.sceneManager.changeSceneTo(Constants.MENU_SCENE)
            
    def checkCollisionPlayerCoin(self, coin):
        collision_tolerance = 10
        player = self.player
        if not player.visible: return
        if not coin.visible: return
        coin_rect = pygame.Rect(player.x, player.y,
                                    player.width, player.height)
        enemy_rect = pygame.Rect(coin.x, coin.y,
                                coin.width, coin.height)
        if coin_rect.colliderect(enemy_rect):
            coin.active = False
            coin.visible = False
            self.play_sound(self.score_sound)
            ScoreLabel.score += 1
            
    def checkCollisionPlayerItem(self, item):
        collision_tolerance = 10
        player = self.player
        if not player.visible: return
        if not item.visible: return
        coin_rect = pygame.Rect(player.x, player.y,
                                    player.width, player.height)
        item_rect = pygame.Rect(item.x, item.y,
                                item.width, item.height)
        if coin_rect.colliderect(item_rect):
            item.active = False
            item.visible = False
            
    # def checkCollisionBulletWall2(self, bullets):
    #     collision_tolerance = 10
    #     for bullet in bullets:
    #         if bullet.visible:
    #             bullet_rect = pygame.Rect(bullet.x, bullet.y,
    #                                       bullet.width, bullet.height)
    #             wall_rect = pygame.Rect(self.wall.x, self.wall.y,
    #                                     self.wall.width, self.wall.height)
    #             if bullet_rect.colliderect(wall_rect):
    #                 bullet.collide += 1
    #                 if abs(wall_rect.top - bullet_rect.bottom) < collision_tolerance and bullet.vy > 0:
    #                     bullet.vy *= -1
    #                 if abs(wall_rect.bottom - bullet_rect.top) < collision_tolerance and bullet.vy < 0:
    #                     bullet.vy *= -1
    #                 if abs(wall_rect.right - bullet_rect.left) < collision_tolerance and bullet.vx < 0:
    #                     bullet.vx *= -1
    #                 if abs(wall_rect.left - bullet_rect.right) < collision_tolerance and bullet.vy > 0:
    #                     bullet.vx *= -1

    # def checkCollisionBulletTank(self, bullets, tank):
    #     for bullet in bullets:
    #         if bullet.visible:
    #             bullet_rect = pygame.Rect(bullet.x, bullet.y,
    #                                       bullet.width, bullet.height)
    #             tank_rect = pygame.Rect(tank.x, tank.y,
    #                                     tank.width, tank.height)
    #             if bullet_rect.colliderect(tank_rect):
    #                 bullet.active = False
    #                 bullet.visible = False
    #                 bullet.x = -100
    #                 if bullet.color == 1 and (tank.type == TankType.ENEMY_1 or tank.type == TankType.PLAYER_2 or tank.type == TankType.AI_2):
    #                     ScoreLabel.score += 1
    #                 if bullet.color == 2 and (tank.type == TankType.PLAYER_1 or tank.type == TankType.AI_1):
    #                     ScoreLabel2.score += 1
