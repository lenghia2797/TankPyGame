import pygame


class Loader:
    def __init__(self):
        self.background_image = pygame.image.load(
            r'./assets/images/background.png')
        self.play_button_image = pygame.image.load(
            r'./assets/images/first_play_button.png')

        self.tank_blue_image = pygame.image.load(
            r'./assets/images/tank-blue-2.png')
        self.tank_red_image = pygame.image.load(
            r'./assets/images/tank-red-2.png')
        self.tank_yellow_image = pygame.image.load(
            r'./assets/images/tank-yellow-2.png')
        self.circle_1_image = pygame.image.load(
            r'./assets/images/circle_1.png')
        self.barrel_blue_image = pygame.image.load(
            r'./assets/images/barrel-blue.png')
        self.barrel_red_image = pygame.image.load(
            r'./assets/images/barrel-red.png')
        self.barrel_yellow_image = pygame.image.load(
            r'./assets/images/barrel-yellow.png')
        self.bullet_blue_image = pygame.image.load(
            r'./assets/images/bullet-blue.png')
        self.bullet_red_image = pygame.image.load(
            r'./assets/images/bullet-red.png')
        self.bullet_yellow_image = pygame.image.load(
            r'./assets/images/bullet-yellow.png')
        self.triangle_image = pygame.image.load(
            r'./assets/images/triangle.png')
        self.wall_image = pygame.image.load(r'./assets/images/wall.png')
        
        self.new_game_image = pygame.image.load(r'./assets/images/img_new_game.png')
        self.start_image = pygame.image.load(r'./assets/images/img_start.png')
        
        
        self.coin_image = pygame.image.load(r'./assets/images/coin.png')