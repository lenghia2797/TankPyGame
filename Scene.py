import pygame
from GameObject import GameObject
from InputHandler import InputHandler
from Loader import Loader
from Renderer import Renderer


class Scene:
    def __init__(self, screen):
        self.screen = screen
        self.renderer: Renderer = Renderer(self)
        self.inputHandler: InputHandler = InputHandler(self)
        self.loader: Loader = Loader()
        
        self.objects: GameObject[100] = []
        
    def add(self, object: GameObject):
        self.objects.append(object)
        self.renderer.sort(object)
        
    def create(self):
        pass
    
    def update(self):
        m_x, m_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.inputHandler.process(m_x, m_y)
                
        self.renderer.render()
        
        return True
        