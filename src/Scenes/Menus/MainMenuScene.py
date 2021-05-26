from src.Components.ComponentManager import ComponentManager


class MainMenuScene:
    def __init__(self):
        self.component_manager = ComponentManager()

    def load(self):
        self.component_manager.add_component("ButtonComponent",
                                             text="Pseudo: ", position=(100, 100),
                                             font_name="arial", font_size=30,
                                             action=[]
        )

        self.component_manager.load_component()

    def update(self, event):
        self.component_manager.update_component(event)

    def render(self, window):
        self.component_manager.render_component(window)
