import pygame


class TextComponent:
    def __init__(self, args):
        self.args = args

        self.text = self.args.get("text", "Default text")
        self.position = self.args.get("position", (0, 0))
        self.text_color = self.args.get("text_color", "white")

        self.font_name = self.args.get("font_name", "arial")
        self.font_size = self.args.get("font_size", 30)

        self.surface = None
        self.surface_rect = None

    def load(self):
        self.surface = pygame.font.SysFont(self.font_name, self.font_size).render(self.text, False, self.text_color)

        self.surface_rect = self.surface.get_rect()

        self.surface_rect.x, self.surface_rect.y = self.position

    def update(self, event):
        pass

    def render(self, window):
        window.blit(self.surface, self.surface_rect)
