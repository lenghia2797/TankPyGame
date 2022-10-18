from Constants import Constants
from gamecore.Game import Game
from gamecore.Scene import Scene
from gamecore.SceneManager import SceneManager


class MenuScene(Scene):
    def __init__(self, screen, game: Game, sceneManager: SceneManager):
        super().__init__(screen, game, sceneManager)
        self.name = Constants.MENU_SCENE