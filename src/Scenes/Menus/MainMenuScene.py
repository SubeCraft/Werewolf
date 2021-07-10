import pygame, sys

from src.Components.ComponentManager import ComponentManager


class MainMenuScene:
    def __init__(self):
        self.component_manager = ComponentManager()

    def load(self):
        from src.utils.constant import WIDTH, HEIGHT, FONT_PATH

        self.component_manager.add_component("ButtonComponent", text="Crée une partie",
                                             position=(WIDTH/2.50, HEIGHT/2.65), text_color="#492B12",
                                             font_name=FONT_PATH, font_size=70,
                                             action=[{"builtin": "switch_scene", "args": ["CreateGameMenuScene"]}]
                                             )
        self.component_manager.add_component("ButtonComponent", text="Rejoindre une partie",
                                             position=(WIDTH/2.60, HEIGHT/1.85), text_color="#492B12",
                                             font_name=FONT_PATH, font_size=70,
                                             action=[{"builtin": "switch_scene", "args": ["JoinGameMenuScene"]}]
                                             )
        self.component_manager.add_component("ButtonComponent", text="Quitter",
                                             position=(WIDTH/2.20, HEIGHT/1.42), text_color="#492B12",
                                             font_name=FONT_PATH, font_size=70,
                                             action=[{"builtin": sys.exit, "args": [0]}]
                                             )

        self.component_manager.load_component()

    def update(self):
        self.component_manager.update_component()

    def render(self, window):
        window.blit(pygame.image.load("assets/img/signs/sign_main_menu.png").convert_alpha(), (0, 0))

        self.component_manager.render_component(window)
