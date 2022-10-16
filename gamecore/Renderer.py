from gamecore.GameObject import GameObject


class Renderer:
    def __init__(self, scene):
        self.scene = scene
    
    def render(self):
        if len(self.scene.objects) > 0:
            for object in self.scene.objects:
                if object.visible and object.active:
                    object.render()
            
    def sortFunc(self, object):
        return object.depth
    
    def sort(self):
        self.scene.objects.sort(key=self.sortFunc)
        
    def destroy(self, object: GameObject):
        for o in self.scene.objects:
            if o is object:
                self.scene.objects.remove(object)