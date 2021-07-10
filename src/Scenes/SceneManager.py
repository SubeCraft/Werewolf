import pygame

from src.Scenes.Menus.MainMenuScene import MainMenuScene
from src.Scenes.Menus.CreateGameMenuScene import CreateGameMenuScene
from src.Scenes.Menus.JoinGameMenuScene import JoinGameMenuScene

from src.Scenes.Game.GameScene import GameScene


class SceneManager:
    def __init__(self):
        self.scenes = {
            "MainMenuScene": MainMenuScene,
            "CreateGameMenuScene": CreateGameMenuScene,
            "JoinGameMenuScene": JoinGameMenuScene,
            "GameScene": GameScene
        }

        self.scene = None

    def switch_scene(self, new_scene):
        self.scene = self.scenes[new_scene]()

    def load_scene(self):
        self.scene.load()

    def render_update_scene(self, window):
        while True:
            window.fill([0, 0, 0])

            self.scene.update()
            self.scene.render(window)

            pygame.display.flip()
