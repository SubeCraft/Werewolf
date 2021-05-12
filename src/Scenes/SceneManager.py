from src.Scenes.MainMenuScene import MainMenuScene


class SceneManager:
    def __init__(self):
        self.scenes = {
            "MainMenuScene": MainMenuScene
        }

        self.scene = None

    def switch_scene(self, new_scene):
        self.scene = self.scenes[new_scene]()
        self.scene.load()

    def update_scene(self, event):
        self.scene.update(event)

    def render_scene(self, window):
        self.scene.render(window)
