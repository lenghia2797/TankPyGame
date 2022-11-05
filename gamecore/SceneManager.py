from Constants import Constants

class SceneManager:
    sceneList = []
    CurrentSceneName = Constants.GAME_SCENE
    def __init__(self, game):
        self.game = game
    
    def changeSceneTo(self, name):
        SceneManager.CurrentSceneName = name
        self.getCurrentScene().run()
        
    def getCurrentScene(self):
        for scene in self.sceneList:
            if scene.name == SceneManager.CurrentSceneName:
                return scene
            
    def update(self):
        return self.getCurrentScene().update()
            