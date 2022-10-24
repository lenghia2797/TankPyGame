from Constants import Constants
from gamecore.Game import Game
from gamecore.GameObject import GameObject
from gamecore.Scene import Scene
from gamecore.SceneManager import SceneManager


class MenuScene(Scene):
    def __init__(self, screen, game: Game, sceneManager: SceneManager):
        super().__init__(screen, game, sceneManager)
        self.name = Constants.MENU_SCENE
        
        self.background = GameObject(self, 0, 0, Constants.SCREEN_WIDTH,
                                     Constants.SCREEN_HEIGHT, self.game.loader.background_image, 0)
        
        self.add(self.background)
        
        self.playBtn = GameObject(self, 0, 0, Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT, self.game.loader.start_image, 1)

        self.add(self.playBtn)