import pygame
from pygame.locals import KEYDOWN, K_BACKSPACE, MOUSEBUTTONDOWN


class InputBoxComponent:
    def __init__(self, args):
        self.args = args

        self.text = ""

        self.label = self.args["label"]
        self.position = self.args["position"]

        self.font_name = self.args["font_name"]
        self.font_size = self.args["font_size"]

        self.surface = None
        self.surface_rect = None
        self.active = False

    def load(self):
        self.surface = pygame.font.SysFont(self.font_name, self.font_size)\
            .render(self.label+self.text, False, [255, 255, 255])

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
