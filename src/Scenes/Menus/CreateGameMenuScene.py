import pygame

from src.Components.ComponentManager import ComponentManager

from src.utils.INIParser import INIParser


class CreateGameMenuScene:
    def __init__(self):
        self.component_manager = ComponentManager()

        self.parser = INIParser("user.ini")

        self.username = None

    def load(self):
        from src.utils.constant import WIDTH, HEIGHT, FONT_PATH

        if self.parser.get_value("user", "username") == "":
            self.username = self.component_manager.add_component("InputBoxComponent", label="Pseudo: ",
                                                                 position=(WIDTH/3.20, HEIGHT/2.65),
                                                                 text_color="#492B12",
                                                                 font_name=FONT_PATH, font_size=70
                                                                 )
        else:
            self.username = self.component_manager.add_component("InputBoxComponent", label="Pseudo: ",
                                                                 text=self.parser.get_value("user", "username"),
                                                                 position=(WIDTH/3.20, HEIGHT/2.65),
                                                                 text_color="#492B12",
                                                                 font_name=FONT_PATH, font_size=70
                                                                 )
        self.component_manager.add_component("InputBoxComponent", label="IP: ",
                                             position=(WIDTH/2.70, HEIGHT/1.85), text_color="#492B12",
                                             font_name=FONT_PATH, font_size=70
                                             )
        self.component_manager.add_component("ButtonComponent", text="Crée la partie",
                                             position=(WIDTH/2.43, HEIGHT/1.42), text_color="#492B12",
                                             font_name=FONT_PATH, font_size=70,
                                             action=[{
                                                     "builtin": self.parser.add_value,
                                                     "args": ["user", "username",
                                                              self.parser.get_value("user", "username")]
                                             }, {"builtin": "switch_scene", "args": ["GameScene"]}])

        self.component_manager.load_component()

    def update(self):
        self.component_manager.update_component()

    def render(self, window):
        window.blit(pygame.image.load("assets/img/signs/sign_create_join_menu.png").convert_alpha(), (0, 0))

        self.component_manager.render_component(window)
