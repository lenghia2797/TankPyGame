
from Tank import Tank


class Player(Tank):
    def __init__(self, screen, x, y, width, height, image, depth):
        super().__init__(screen, x, y, width, height, image, depth)
    
    def update(self):
        super().update()
        
    