from src.Components.ComponentManager import ComponentManager


class GameScene:
    def __init__(self):
        self.component_manager = ComponentManager()

    def load(self):
        from src.utils.constant import WIDTH, HEIGHT, FONT_PATH

        self.component_manager.load_component()

    def update(self):
        self.component_manager.update_component()

    def render(self, window):
        self.component_manager.render_component(window)
