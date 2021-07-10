import pygame
from pygame.locals import FULLSCREEN

from src.Scenes.SceneManager import SceneManager

from src.utils.INIParser import INIParser

from config import WINDOW_SIZE, WINDOW_TITLE


class App:
    def __init__(self):
        self.window = pygame.display.set_mode(WINDOW_SIZE, FULLSCREEN)

        self.scene_manager = SceneManager()

        self.parser = INIParser("user.ini")
        if not self.parser.parser.has_section("user"):
            self.parser.add_section("user")
            self.parser.add_value("user", "username", "")

    def run(self):
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)

        self.scene_manager.switch_scene("MainMenuScene")
        self.scene_manager.load_scene()
        self.scene_manager.render_update_scene(self.window)
