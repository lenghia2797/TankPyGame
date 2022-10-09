
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
        
    def updateByState(self):
        for state in self.states:
            if state == TankState.LEFT:
                self.x -= self.speed
            if state == TankState.RIGHT:
                self.x += self.speed
            if state == TankState.UP:
                self.y -= self.speed
            if state == TankState.DOWN:
                self.y += self.speed
            
    def onReleaseA(self):
        self.states.remove(TankState.LEFT) 
            
    def onReleaseD(self):
        self.states.remove(TankState.RIGHT) 
        
    def onReleaseW(self):
        self.states.remove(TankState.UP) 
        
    def onReleaseS(self):
        self.states.remove(TankState.DOWN) 
    
    def onPressA(self):
        self.states.append(TankState.LEFT) 
            
    def onPressD(self):
        self.states.append(TankState.RIGHT) 
        
    def onPressW(self):
        self.states.append(TankState.UP) 
        
    def onPressS(self):
        self.states.append(TankState.DOWN) 