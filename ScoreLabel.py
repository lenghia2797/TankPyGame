import pygame
from Constants import Constants


class ScoreLabel:
    score = 0

    def __init__(self, scene):
        self.scene = scene
        self.font = pygame.font.Font('freesansbold.ttf', 30)
        self.text = self.font.render(
            f'Score: {ScoreLabel.score}', True, Constants.COLOR_TEXT)
        self.textRect = self.text.get_rect()
        self.textRect.center = (Constants.SCORE_LABEL_X,
                                Constants.SCORE_LABEL_Y)

    def update(self):
        self.render()

    def render(self):
        self.text = self.font.render(
            f'Score: {ScoreLabel.score}', True, Constants.COLOR_TEXT)

        self.scene.screen.blit(self.text, (self.textRect.x +
                                           self.textRect.width/2 - 50, self.textRect.y))


class ScoreLabel2:
    score = 0

    def __init__(self, scene):
        self.scene = scene
        self.font = pygame.font.Font('freesansbold.ttf', 30)
        self.text = self.font.render(
            f'Score: {ScoreLabel.score}', True, Constants.COLOR_TEXT)
        self.textRect = self.text.get_rect()
        self.textRect.center = (Constants.SCORE_LABEL_X,
                                Constants.SCORE_LABEL_Y + 70)

    def update(self):
        self.render()

    def render(self):
        self.text = self.font.render(
            f'Score: {ScoreLabel.score}', True, Constants.COLOR_TEXT)

        self.scene.screen.blit(self.text, (self.textRect.x +
                                           self.textRect.width/2 - 50, self.textRect.y))
