from Enum import TankState
from GameObject import GameObject

class Tank(GameObject):
    def __init__(self, scene, x, y, width, height, image, depth):
        super().__init__(scene, x, y, width, height, image, depth)
        self.states = [TankState.NORMAL]
        self.speed = 3
        
    
    def update(self):
        super().update()
        
    