from pygame import Rect


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
        
    def update(self):
        pass
    
    def render(self):
        self.scene.screen.blit(self.image, (self.x, self.y, self.width, self.height))
    
    def setOnClick(self, onClickFunc):
        self.interactive = True
        self.onClickFunc = onClickFunc
        
    def setKey(self, key, keyFunc):
        self.haveKey = True
        self.keys.append([key, keyFunc])