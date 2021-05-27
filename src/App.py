import pygame, sys

from pygame.locals import QUIT, FULLSCREEN

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

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)

                self.window.fill([0, 0, 0])

                self.scene_manager.update_scene(event)
                self.scene_manager.render_scene(self.window)

                pygame.display.flip()