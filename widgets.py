import pygame as py
from settings import *


class TextBox(py.sprite.Sprite):
    def __init__(self, game, pos):
        self.group = game.ui_sprites
        py.sprite.Sprite.__init__(self, self.group)

        self.font = py.font.Font(None, 36)
        self.text = ''

        self.image = self.font.render(self.text, 1, BLACK)
        self.rect = self.image.get_rect()

        self.pos = pos
        x, y = pos
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.image = self.font.render(self.text, 1, BLACK)
        self.rect = self.image.get_rect()

        x, y = self.pos
        self.rect.x = x
        self.rect.y = y

    def set_text(self, text):
        self.text = text
