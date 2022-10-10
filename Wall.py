from GameObject import GameObject


class Wall(GameObject):
    def __init__(self, scene, x, y, width, height, image, depth):
        super().__init__(scene, x, y, width, height, image, depth)
        
    def update(self):
        super().update()