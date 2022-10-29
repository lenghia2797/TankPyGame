from pygame import Rect
import pygame


class GameObject:
    def __init__(self, scene, x, y, width, height, image, depth):
        self.scene = scene
        self.rect = Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.depth = depth
        self.visible = True
        self.active = True
        self.interactive = False
        self.onClickFunc: Any
        self.haveKey = False
        self.keys = []
        self.ignoreCamera = False
        self.cameraOffsetX = 0
        self.cameraOffsetY = 0

    def update(self):
        pass

    def render(self):
        if self.ignoreCamera:
            self.scene.screen.blit(
            self.image, (self.x, self.y, self.width, self.height))
        else:
            self.scene.screen.blit(
            self.image, (self.x + self.cameraOffsetX, self.y + self.cameraOffsetY, self.width, self.height))

    def setOnClick(self, onClickFunc):
        self.interactive = True
        self.onClickFunc = onClickFunc

    def setKey(self, key, keyFunc):
        self.haveKey = True
        self.keys.append([key, keyFunc])

    def rot_center(self, image, angle):

        loc = image.get_rect().center  # rot_image is not defined
        rot_sprite = pygame.transform.rotate(image, angle)
        rot_sprite.get_rect().center = loc
        return rot_sprite
    
    def setScale(self, x, y):
        self.image = pygame.transform.scale(self.image, (self.width*x, self.height*y))
