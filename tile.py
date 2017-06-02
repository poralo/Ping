import pygame as py
from settings import *


class Tile(py.sprite.Sprite):
    """A Tile which we can change is color"""
    SIZE = 100
    GROUP = py.sprite.Group()

    def __init__(self, pos):
        py.sprite.Sprite.__init__(self, Tile.GROUP)

        self.image = py.Surface((Tile.SIZE, Tile.SIZE))
        self.rect = self.image.get_rect()

        self.pos = pos
        x, y = pos
        self.rect.x = x * Tile.SIZE + PADDLE * (x + 1)
        self.rect.y = y * Tile.SIZE + PADDLE * (y + 1)

        self.state = 0

    def get_pos(self):
        return self.pos

    def change_state(self):
        self.state = not self.state

    def update(self):
        if self.state:
            self.image.fill(WHITE)
        else:
            self.image.fill(BLACK)


class Grid:
    """A grid which in containing Tile"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

        w = width * Tile.SIZE + PADDLE * (width + 1)
        h = height * Tile.SIZE + PADDLE * (height + 1)
        self.surface = py.Surface((w, h))
        self.surface.fill(GREEN)

        self.create_grid()
        self.change = True

        self.x = 0
        self.y = 0

    def neighbour_tiles(self, target):
        tiles = []
        neighbours = []
        for x in range(target.pos[0] - 1, target.pos[0] + 2):
            for y in range(target.pos[1] - 1, target.pos[1] + 2):
                if (x, y) != target.pos and 0 <= x <= self.width and 0 <= y <= self.height:
                    neighbours.append((x, y))
        for tile in Tile.GROUP:
            if tile.pos in neighbours:
                tiles.append(tile)

        return tiles

    def clicked(self):
        if not py.mouse.get_pressed()[0]:
            self.change = True

        mx, my = py.mouse.get_pos()
        for tile in Tile.GROUP:
            if tile.rect.collidepoint((mx, my)):
                if py.mouse.get_pressed()[0] & self.change:
                    self.change = False

                    for t in self.neighbour_tiles(tile):
                        t.change_state()

    def create_grid(self):
        for y in range(self.height):
            for x in range(self.width):
                Tile((x, y))

    def update(self):
        self.clicked()

        Tile.GROUP.update()
        Tile.GROUP.draw(self.surface)

    def draw(self, surface):
        surface.blit(self.surface, (self.x, self.y))
