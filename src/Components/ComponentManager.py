from src.Components.TextComponent import TextComponent
from src.Components.InputBoxComponent import InputBoxComponent
from src.Components.ButtonComponent import ButtonComponent


class ComponentManager:
    def __init__(self):
        self.components = {}

        self.id_component = 0

    def load_component(self):
        for component in self.components.values():
            component.load()

    def update_component(self, event):
        for component in self.components.values():
            component.update(event)

    def render_component(self, window):
        for component in self.components.values():
            component.render(window)

    def add_component(self, name_component, **component_args):
        component_class = globals()[name_component](component_args)

        self.components[name_component+str(self.id_component)] = component_class
        self.id_component += 1

        return component_class
