import pygame
from Constants import Constants


class ScoreLabel:
    score = 0

    def __init__(self, scene):
        self.scene = scene
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

        self.scene.screen.blit(self.text, (self.textRect.x +
                                           self.textRect.width/2 - 50, self.textRect.y))
