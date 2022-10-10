import math
from Constants import Constants
# from tkinter import HIDDEN
from Enum import MoleStatus, MoleType, SceneKeys
import pygame
import time
import sys

import random
from enum import Enum
from pygame import mixer
from GameObject import GameObject
from GameScene import GameScene

from spritesheet import SpriteSheet

pygame.init()

screen = pygame.display.set_mode(
    (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
pygame.display.set_caption('Tank')

font = pygame.font.Font('freesansbold.ttf', 30)


# mixer.init()
# mixer.music.set_volume(0.1)

# mixer.music.load('assets/sounds/bgm.mp3')
class ScoreLabel:
    score = 0

    def __init__(self):
        self.text = font.render(
            f'Score: {ScoreLabel.score}', True, Constants.COLOR_TEXT)
        self.textRect = self.text.get_rect()
        self.textRect.center = (Constants.SCORE_LABEL_X,
                                Constants.SCORE_LABEL_Y)

    def update(self):
        self.render()

    def render(self):
        self.text = font.render(
            f'Score: {ScoreLabel.score}', True, Constants.COLOR_TEXT)

        screen.blit(self.text, (self.textRect.x +
                    self.textRect.width/2 - 50, self.textRect.y))


# class PlayButton:
#     def __init__(self):
#         self.x = Constants.SCREEN_WIDTH/2 - Constants.PLAY_BUTTON_WIDTH/2 + 50
#         self.y = Constants.SCREEN_HEIGHT*0.6
#         self.visible = True

#     def update(self):
#         self.render()

#     def render(self):
#         if (self.visible):
#             screen.blit(play_button_image, (self.x, self.y))


def isTouchOnRect(x, y, rectX, rectY, rectWidth, rectHeight):
    if rectX < x and x < rectX + rectWidth and rectY < y and y < rectY + rectHeight:
        return True
    return False


def main():
    currentScene = SceneKeys.MENU_SCENE
    showTimeOver = False
    gameOver = True
    running = True

    clock = pygame.time.Clock()
    scoreLabel = ScoreLabel()
    # playButton = PlayButton()
    FPS = 60

    lastTime = pygame.time.get_ticks()
    deltaTime = 0

    lastTimeExplode = pygame.time.get_ticks()
    lastTimeShowPlay = pygame.time.get_ticks()

    # mixer.music.play(-1)

    gameScene = GameScene(screen)

    while running:
        clock.tick(FPS)
        now = pygame.time.get_ticks()
        deltaTime = now - lastTime
        lastTime = pygame.time.get_ticks()
        # print(deltaTime)

        # m_x, m_y = pygame.mouse.get_pos()

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         running = False
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         if (currentScene == Scene.GAME_SCENE and not gameOver):
        #             # total_hit += 1
        #             pass
        # if (currentScene == Scene.GAME_SCENE):
        #     pass
        # elif (currentScene == Scene.MENU_SCENE):
        #     if ((pygame.time.get_ticks() - lastTimeShowPlay > 700) and isTouchOnRect(m_x, m_y, playButton.x, playButton.y, Constants.PLAY_BUTTON_WIDTH, Constants.PLAY_BUTTON_HEIGHT)):
        #         gameOver = False
        #         currentScene = Scene.GAME_SCENE
        #         ScoreLabel.score = 0
        #         playButton.visible = False

        running = gameScene.update()
        scoreLabel.update()

        # if (currentScene == Scene.MENU_SCENE):
        #     pass
        # if (pygame.time.get_ticks() - lastTimeShowPlay > 700):
        #     playButton.update()
        # if (gameOver and currentScene == Scene.GAME_SCENE):
        #     pass
        pygame.display.flip()
    pygame.quit()


main()
