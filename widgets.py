import pygame as py
from settings import *


class TextBox(py.sprite.Sprite):
    def __init__(self, game, pos):
        self.group = game.ui_sprites, game.allsprites
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


class PauseScreen:
    def __init__(self, game):
        self.game = game
        self.background = py.Surface((WIDTH, HEIGHT))
        self.background.set_alpha(150)
        self.background.fill((0, 0, 0))

        self.font = py.font.Font(None, 100)
        self.image = self.font.render('Paused', 1, RED)

    def draw(self):
        self.game.screen.blit(self.background, (0, 0))
        mid = self.image.get_rect().center
        self.game.screen.blit(self.image, (WIDTH / 2 - mid[0], HEIGHT / 2 - mid[1]))

