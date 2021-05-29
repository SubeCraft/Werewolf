import pygame
from pygame.locals import MOUSEBUTTONDOWN


class ButtonComponent:
    def __init__(self, args):
        self.args = args

        self.text = self.args["text"]
        self.position = self.args["position"]

        self.font_name = self.args["font_name"]
        self.font_size = self.args["font_size"]

        self.action = self.args["action"]

        self.surface = None
        self.surface_rect = None

    def load(self):
        self.surface = pygame.font.SysFont(self.font_name, self.font_size).render(self.text, False, [255, 255, 255])

        self.surface_rect = self.surface.get_rect()

        self.surface_rect.x, self.surface_rect.y = self.position

    def update(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.surface_rect.collidepoint(event.pos):
                for action in self.action:
                    if not action["args"]:
                        action["builtin"]()
                    else:
                        for action_arg in action["args"]:
                            action["builtin"](action_arg)

    def render(self, window):
        window.blit(self.surface, self.surface_rect)
