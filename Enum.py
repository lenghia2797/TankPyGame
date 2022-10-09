from enum import Enum

class MoleStatus(Enum):
    HIDDEN = 0
    SHOW_UP = 1
    EXIT = 2
    WAITING = 3
    NOT_START = 4
    
class MoleType(Enum):
    NORMAL = 0
    NORMAL_2 = 1
    NORMAL_3 = 2
    BOMB = 3
    
class SceneKeys(Enum):
    MENU_SCENE = 0
    GAME_SCENE = 1
    
class TankState(Enum):
    NORMAL = 0
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4