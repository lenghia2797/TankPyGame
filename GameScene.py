import random
import pygame
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
        
        self.create()
        
    def create(self):
        super().create()
        background = GameObject(self, 0, 0, Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT, self.loader.background_image, 0)
        player = Player(self, 100, 100, Constants.TANK_WIDTH, Constants.TANK_HEIGHT, self.loader.tank_yellow_image, 3)
        player.setOnClick(onClickPlayer)
        self.add(background)
        self.add(player)
        
    def update(self):
        running = super().update()
        
        
        return running