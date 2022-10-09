
import math
from xml.etree.ElementInclude import include
import pygame
from Bullet import Bullet
from Constants import Constants
from Enum import TankState
from Loader import Loader
from Tank import Tank

class Player(Tank):
    def __init__(self, scene, x, y, width, height, image, depth):
        super().__init__(scene, x, y, width, height, image, depth)
    
    def update(self):
        super().update()
        self.updateByState()
        
    def rot_center(self, image, angle, x, y):
        
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

        return rotated_image, new_rect
    
    # def rot_center(self, image, rect, angle):
    #     rot_image = pygame.transform.rotate(image, angle)
    #     rot_rect = rot_image.get_rect(center=rect.center)
    #     return rot_image,rot_rect
        
    def updateByState(self):
        for state in self.states:
            if state == TankState.ROTATE_LEFT:
                self.setAngle(self.angle + 5)
                # self.image, self.rect = self.rot_center(self.scene.loader.tank_red_image, self.rect, self.angle)
                self.image, self.rect = self.rot_center(self.scene.loader.tank_red_image, self.angle, self.x + Constants.TANK_WIDTH/2, self.y+ Constants.TANK_HEIGHT/2)
            if state == TankState.ROTATE_RIGHT:
                self.setAngle(self.angle - 5)
                # self.image, self.rect = self.rot_center(self.scene.loader.tank_red_image, self.rect, self.angle)
                self.image, self.rect = self.rot_center(self.scene.loader.tank_red_image, self.angle, self.x, self.y)
            if state == TankState.UP:
                self.y += self.speed * math.cos(self.angle * math.pi / 180)
                self.x += self.speed * math.sin(self.angle * math.pi / 180)
                # self.rect.x = self.x
                # self.rect.y = self.y
            if state == TankState.DOWN:
                self.y -= self.speed * math.cos(self.angle * math.pi / 180)
                self.x -= self.speed * math.sin(self.angle * math.pi / 180)
                # self.rect.x = self.x
                # self.rect.y = self.y
            
    def onReleaseA(self):
        self.states.remove(TankState.ROTATE_LEFT) 
            
    def onReleaseD(self):
        self.states.remove(TankState.ROTATE_RIGHT) 
        
    def onReleaseW(self):
        self.states.remove(TankState.UP) 
        
    def onReleaseS(self):
        self.states.remove(TankState.DOWN) 
    
    def onPressA(self):
        self.states.append(TankState.ROTATE_LEFT)
            
    def onPressD(self):
        self.states.append(TankState.ROTATE_RIGHT) 
        
    def onPressW(self):
        self.states.append(TankState.UP) 
        
    def onPressS(self):
        self.states.append(TankState.DOWN) 