import math
# from tkinter import HIDDEN
from Enum import MoleStatus, MoleType, Scene
import pygame
import time
import sys

import random
from enum import Enum
from pygame import mixer

from spritesheet import SpriteSheet


pygame.init()
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Hit Mole')
GREY = (150,150,150)
WHITE = (255,255,255)
BLACK = (0,0,0)
COLOR1 = (66, 135, 245)
COLOR2 = (235, 158, 52)
COLOR3 = (232, 58, 28)
font = pygame.font.Font('freesansbold.ttf', 30)


mixer.init()
mixer.music.set_volume(0.1)

mixer.music.load('sounds/bgm.mp3')

background_image = pygame.image.load(r'./images/background.jpeg')
play_button_image = pygame.image.load(r'./images/first_play_button.png')

tank_blue_image = pygame.image.load(r'./images/tank-blue.png')
tank_red_image = pygame.image.load(r'./images/tank-red.png')
tank_yellow_image = pygame.image.load(r'./images/tank-yellow.png')
circle_1_image = pygame.image.load(r'./images/circle_1.png')
barrel_blue_image = pygame.image.load(r'./images/barrel-blue.png')
barrel_red_image = pygame.image.load(r'./images/barrel-red.png')
barrel_yellow_image = pygame.image.load(r'./images/barrel-yellow.png')

SCORE_LABEL_X = 100
SCORE_LABEL_Y = 150
PADDING_LABEL = 75
COLOR_TEXT = (204, 102, 255)

PLAY_BUTTON_WIDTH = 296
PLAY_BUTTON_HEIGHT = 116

TANK_WIDTH = 83
TANK_HEIGHT = 78
BULLET_WIDTH = 72
BULLET_HEIGHT = 72

class GameObject:
    def __init__(self, x, y, width, height, image, depth):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.depth = depth
        self.visible = True
        self.active = True
    
    def update(self):
        pass
    
    def render(self):
        screen.blit(self.image, (self.x, self.y))
        
class Renderer:
    def __init__(self):
        self.objects: GameObject[10] = []
    
    def render(self):
        if len(self.objects) > 0:
            for object in self.objects:
                if object.visible:
                    object.render()
            
    def sortFunc(self, object):
        return object.depth
    
    def add(self, object: GameObject):
        self.objects.append(object)
        self.objects.sort(key=self.sortFunc)
        
class Tank(GameObject):
    def __init__(self, x, y, width, height, image, depth):
        super().__init__(x, y, width, height, image, depth)
    
    def update(self):
        super().update()

class ScoreLabel:
    score = 0
    def __init__(self):
        self.text = font.render(f'Score: {ScoreLabel.score}', True, COLOR_TEXT)
        self.textRect = self.text.get_rect()
        self.textRect.center = (SCORE_LABEL_X, SCORE_LABEL_Y)
        
    def update(self):
        self.render()
    
    def render(self):
        self.text = font.render(f'Score: {ScoreLabel.score}', True, COLOR_TEXT)
        
        screen.blit(self.text, (self.textRect.x + self.textRect.width/2 - 50, self.textRect.y))

class PlayButton:
    def __init__(self):
        self.x = SCREEN_WIDTH/2 - PLAY_BUTTON_WIDTH/2 + 50
        self.y = SCREEN_HEIGHT*0.6
        self.visible = True
        
    def update(self):
        self.render()
    
    def render(self):
        if (self.visible):
            screen.blit(play_button_image, (self.x, self.y))

def isTouchOnRect(x, y, rectX, rectY, rectWidth, rectHeight):
    if rectX < x and x < rectX + rectWidth and rectY < y and y < rectY + rectHeight:
        return True
    return False

def main():
    currentScene = Scene.MENU_SCENE
    showTimeOver = False
    gameOver = True
    running = True
    
    clock = pygame.time.Clock()
    scoreLabel = ScoreLabel()
    playButton = PlayButton()
    FPS = 20
    
    lastTime = pygame.time.get_ticks()
    deltaTime = 0
    
    lastTimeExplode = pygame.time.get_ticks()
    lastTimeShowPlay = pygame.time.get_ticks()
    
    mixer.music.play(-1)
    
    renderer = Renderer()
    
    background = GameObject(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, background_image, 0)
    player = Tank(100, 100, TANK_WIDTH, TANK_HEIGHT, tank_yellow_image, 3)
    
    renderer.add(player)
    renderer.add(background)
    while running:
        clock.tick(FPS)
        now = pygame.time.get_ticks()
        deltaTime = now - lastTime
        lastTime = pygame.time.get_ticks()
        # print(deltaTime)
            
        screen.fill(GREY)
        m_x, m_y = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (currentScene == Scene.GAME_SCENE and not gameOver):
                    total_hit += 1
        if (currentScene == Scene.GAME_SCENE):                
            pass
        elif (currentScene == Scene.MENU_SCENE):
            if ((pygame.time.get_ticks() - lastTimeShowPlay > 700) and isTouchOnRect(m_x, m_y, playButton.x, playButton.y, PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT)):
                gameOver = False
                currentScene = Scene.GAME_SCENE
                ScoreLabel.score = 0
                playButton.visible = False
             
        renderer.render()   
        scoreLabel.update()
        
        
        if (currentScene == Scene.MENU_SCENE):
            pass
        if (pygame.time.get_ticks() - lastTimeShowPlay > 700):
            playButton.update()
        if (gameOver and currentScene == Scene.GAME_SCENE):
            pass
        pygame.display.flip()
    pygame.quit()
    
main()