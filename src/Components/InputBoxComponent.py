import pygame
from pygame.locals import KEYDOWN, K_BACKSPACE, MOUSEBUTTONDOWN


class InputBoxComponent:
    def __init__(self, args):
        self.args = args

        self.text = ""

        self.label = self.args.get("label", "Default label")
        self.position = self.args.get("position", (0, 0))
        self.text_color = self.args.get("text_color", "white")

        self.font_name = self.args.get("font_name", "arial")
        self.font_size = self.args.get("font_size", 30)

        self.surface = None
        self.surface_rect = None
        self.active = False

    def load(self):
        self.surface = pygame.font.SysFont(self.font_name, self.font_size)\
            .render(self.label+self.text, False, self.text_color)

        self.surface_rect = self.surface.get_rect()

        self.surface_rect.x, self.surface_rect.y = self.position

    def update(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.surface_rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        if event.type == KEYDOWN:
            if self.active:
                if event.key == K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

                self.surface = pygame.font.SysFont(self.font_name, self.font_size)\
                    .render(self.label+self.text, False, [255, 255, 255])
        print(self.text)

    def render(self, window):
        window.blit(self.surface, self.surface_rect)
