import pygame
from pygame.locals import FULLSCREEN

from src.Scenes.SceneManager import SceneManager

from config import WINDOW_SIZE, WINDOW_TITLE


class App:
    def __init__(self):
        self.window = pygame.display.set_mode(WINDOW_SIZE, FULLSCREEN)

        self.scene_manager = SceneManager()

    def run(self):
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)

        self.scene_manager.switch_scene("MainMenuScene")
        self.scene_manager.load_scene()
        self.scene_manager.render_update_scene(self.window)
