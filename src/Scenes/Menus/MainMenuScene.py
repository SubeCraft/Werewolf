import pygame, sys

from src.Components.ComponentManager import ComponentManager


class MainMenuScene:
    def __init__(self):
        self.component_manager = ComponentManager()

    def load(self):
        from src.utils.constant import WIDTH, HEIGHT
        self.component_manager.add_component("ButtonComponent", text="Crée une partie",
                                             position=(WIDTH/2.50, HEIGHT/2.65), text_color="#492B12",
                                             font_name="LibreFranklin-Bold", font_size=70,
                                             action=[]
                                             )
        self.component_manager.add_component("ButtonComponent", text="Rejoindre une partie",
                                             position=(WIDTH/2.60, HEIGHT/1.85), text_color="#492B12",
                                             font_name="LibreFranklin-Bold", font_size=70,
                                             action=[]
                                             )
        self.component_manager.add_component("ButtonComponent", text="Quitter",
                                             position=(WIDTH/2.20, HEIGHT/1.40), text_color="#492B12",
                                             font_name="LibreFranklin-Bold", font_size=70,
                                             action=[{"builtin": sys.exit, "args": [0]}]
                                             )

        self.component_manager.load_component()

    def update(self, event):
        self.component_manager.update_component(event)

    def render(self, window):
        window.blit(pygame.image.load("assets/img/signs/sign_main_menu.png").convert_alpha(), (0, 0))

        self.component_manager.render_component(window)
