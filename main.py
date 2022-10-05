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


SCORE_LABEL_X = 100
SCORE_LABEL_Y = 150
PADDING_LABEL = 75
COLOR_TEXT = (204, 102, 255)

PLAY_BUTTON_WIDTH = 296
PLAY_BUTTON_HEIGHT = 116

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
    while running:
        clock.tick(FPS)
        now = pygame.time.get_ticks()
        deltaTime = now - lastTime
        lastTime = pygame.time.get_ticks()
        # print(deltaTime)
            
        screen.fill(GREY)
        m_x, m_y = pygame.mouse.get_pos()
        screen.blit(background_image, (0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (currentScene == Scene.GAME_SCENE and not gameOver):
                    total_hit += 1
        if (currentScene == Scene.GAME_SCENE):                
            pass
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