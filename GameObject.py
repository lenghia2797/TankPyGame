class GameObject:
    def __init__(self, scene, x, y, width, height, image, depth):
        self.scene = scene
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.depth = depth
        self.visible = True
        self.active = True
        self.interactive = False
        self.onClickFunc : Any
    
    def update(self):
        pass
    
    def render(self):
        self.scene.screen.blit(self.image, (self.x, self.y))
    
    def setOnClick(self, onClickFunc):
        self.interactive = True
        self.onClickFunc = onClickFunc