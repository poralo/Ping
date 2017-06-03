import pygame as py
from level_interaction import load_level
from settings import *


class Tile(py.sprite.Sprite):
    """A Tile which we can change is color"""
    def __init__(self, game, state, pos):
        self.group = game.tile_sprites
        py.sprite.Sprite.__init__(self, self.group)
        self.game = game

        self.image = py.Surface((TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()

        self.pos = pos
        x, y = pos
        self.rect.x = x * TILE_SIZE + PADDLE * (x + 1)
        self.rect.y = y * TILE_SIZE + PADDLE * (y + 1)

        self.state = state

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
    def __init__(self, game, level_name):
        self.level = load_level(level_name)
        self.width = len(self.level[0])
        self.height = len(self.level)

        self.game = game

        w = self.width * TILE_SIZE + PADDLE * (self.width + 1)
        h = self.height * TILE_SIZE + PADDLE * (self.height + 1)
        self.surface = py.Surface((w, h))
        self.surface.fill(GREEN)

        mid = self.surface.get_rect().center
        self.x = WIDTH / 2 - mid[0]
        self.y = HEIGHT / 2 - mid[1]

        self.create_grid()
        self.change = True

    def neighbour_tiles(self, target):
        tiles = []
        neighbours = []
        for x in range(target.pos[0] - 1, target.pos[0] + 2):
            for y in range(target.pos[1] - 1, target.pos[1] + 2):
                if (x, y) != target.pos and 0 <= x <= self.width and 0 <= y <= self.height:
                    neighbours.append((x, y))
        for tile in self.game.tile_sprites:
            if tile.pos in neighbours:
                tiles.append(tile)

        return tiles

    def clicked(self):
        if not py.mouse.get_pressed()[0] and not py.mouse.get_pressed()[2]:
            self.change = True

        mx, my = py.mouse.get_pos()
        for tile in self.game.tile_sprites:
            if tile.rect.collidepoint((mx, my)):
                if py.mouse.get_pressed()[0] & self.change:
                    self.change = False
                    self.game.try_number += 1

                    for t in self.neighbour_tiles(tile):
                        t.change_state()

                elif py.mouse.get_pressed()[2] & self.change & DEBUG:
                    self.change = False
                    tile.change_state()

    def create_grid(self):
        for y in range(len(self.level)):
            for x in range(len(self.level[0])):
                tile = Tile(self.game, self.level[y][x], (x, y))
                tile.rect.x += self.x
                tile.rect.y += self.y

    def is_completed(self):
        """Check if the grid is all gold: return bool"""
        completed = 0
        for tile in self.game.tile_sprites:
            if tile.state:
                completed += 1
        all_completed = len(self.level) * len(self.level[0])
        return completed == all_completed

    def update(self):
        self.clicked()
        self.game.tile_sprites.update()

    def draw(self, surface):
        surface.blit(self.surface, (self.x, self.y))
        self.game.tile_sprites.draw(self.game.screen)

