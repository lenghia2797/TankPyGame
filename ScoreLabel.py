import pygame
from Constants import Constants


class ScoreLabel:
    score = 0

    def __init__(self, scene):
        self.scene = scene
        self.font = pygame.font.Font('freesansbold.ttf', 30)
        self.text = self.font.render(
            f'Score: {ScoreLabel.score}', True, (247, 21, 5))
        self.textRect = self.text.get_rect()
        self.textRect.center = (Constants.SCORE_LABEL_X,
                                Constants.SCORE_LABEL_Y)

    def update(self):
        self.render()

    def render(self):
        self.text = self.font.render(
            f'Score: {ScoreLabel.score}', True, (247, 21, 5))

        self.scene.screen.blit(self.text, (self.textRect.x +
                                           self.textRect.width/2 - 50, self.textRect.y))


class ScoreLabel2:
    score = 0

    def __init__(self, scene):
        self.scene = scene
        self.font = pygame.font.Font('freesansbold.ttf', 30)
        self.text = self.font.render(
            f'Score: {ScoreLabel2.score}', True, (12, 189, 242))
        self.textRect = self.text.get_rect()
        self.textRect.center = (Constants.SCORE_LABEL_X + 800,
                                Constants.SCORE_LABEL_Y)

    def update(self):
        self.render()

    def render(self):
        self.text = self.font.render(
            f'Score: {ScoreLabel2.score}', True, (12, 189, 242))

        self.scene.screen.blit(self.text, (self.textRect.x +
                                           self.textRect.width/2 - 50, self.textRect.y))
