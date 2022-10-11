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
        self.renderer.sort()

    def update(self):
        m_x, m_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.inputHandler.process(m_x, m_y)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.inputHandler.process(m_x, m_y, 'down_a')
                if event.key == pygame.K_d:
                    self.inputHandler.process(m_x, m_y, 'down_d')
                if event.key == pygame.K_w:
                    self.inputHandler.process(m_x, m_y, 'down_w')
                if event.key == pygame.K_s:
                    self.inputHandler.process(m_x, m_y, 'down_s')
                if event.key == pygame.K_x:
                    self.inputHandler.process(m_x, m_y, 'down_x')
                if event.key == pygame.K_q:
                    self.inputHandler.process(m_x, m_y, 'down_q')

                if event.key == pygame.K_LEFT:
                    self.inputHandler.process(m_x, m_y, 'down_left')
                if event.key == pygame.K_RIGHT:
                    self.inputHandler.process(m_x, m_y, 'down_right')
                if event.key == pygame.K_UP:
                    self.inputHandler.process(m_x, m_y, 'down_up')
                if event.key == pygame.K_DOWN:
                    self.inputHandler.process(m_x, m_y, 'down_down')
                if event.key == pygame.K_KP_ENTER:
                    self.inputHandler.process(m_x, m_y, 'down_enter')
                if event.key == pygame.K_o:
                    self.inputHandler.process(m_x, m_y, 'down_o')
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.inputHandler.process(m_x, m_y, 'up_a')
                if event.key == pygame.K_d:
                    self.inputHandler.process(m_x, m_y, 'up_d')
                if event.key == pygame.K_w:
                    self.inputHandler.process(m_x, m_y, 'up_w')
                if event.key == pygame.K_s:
                    self.inputHandler.process(m_x, m_y, 'up_s')
                if event.key == pygame.K_x:
                    self.inputHandler.process(m_x, m_y, 'up_x')

                if event.key == pygame.K_LEFT:
                    self.inputHandler.process(m_x, m_y, 'up_left')
                if event.key == pygame.K_RIGHT:
                    self.inputHandler.process(m_x, m_y, 'up_right')
                if event.key == pygame.K_UP:
                    self.inputHandler.process(m_x, m_y, 'up_up')
                if event.key == pygame.K_DOWN:
                    self.inputHandler.process(m_x, m_y, 'up_down')
                if event.key == pygame.K_KP_ENTER:
                    self.inputHandler.process(m_x, m_y, 'up_enter')
                if event.key == pygame.K_o:
                    self.inputHandler.process(m_x, m_y, 'up_o')
        self.updateObjects()
        self.renderer.render()

        return True

    def updateObjects(self):
        for object in self.objects:
            if object.active:
                object.update()
