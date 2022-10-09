class InputHandler:
    def __init__(self, scene):
        self.scene = scene
    
    def process(self, x, y, key = None):
        for object in self.scene.objects: 
            if object.interactive:
                if self.isTouchOnRect(x, y, object.x, object.y, object.width, object.height):
                    object.onClickFunc()
                    break
            if object.haveKey:
                for (k, keyFunc) in object.keys:
                    if k == key:
                        keyFunc()
                    
    def isTouchOnRect(self, x, y, rectX, rectY, rectWidth, rectHeight):
        if rectX < x and x < rectX + rectWidth and rectY < y and y < rectY + rectHeight:
            return True
        return False     