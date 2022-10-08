import pygame


class Loader:
    def __init__(self):
        self.background_image = pygame.image.load(r'./assets/images/background.jpeg')
        self.play_button_image = pygame.image.load(r'./assets/images/first_play_button.png')

        self.tank_blue_image = pygame.image.load(r'./assets/images/tank-blue.png')
        self.tank_red_image = pygame.image.load(r'./assets/images/tank-red.png')
        self.tank_yellow_image = pygame.image.load(r'./assets/images/tank-yellow.png')
        self.circle_1_image = pygame.image.load(r'./assets/images/circle_1.png')
        self.barrel_blue_image = pygame.image.load(r'./assets/images/barrel-blue.png')
        self.barrel_red_image = pygame.image.load(r'./assets/images/barrel-red.png')
        self.barrel_yellow_image = pygame.image.load(r'./assets/images/barrel-yellow.png')