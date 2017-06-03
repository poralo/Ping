import pygame as py
from sys import exit
from settings import *
from tile import Grid
from widgets import TextBox


class Game:
    """Main class for the game"""
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode((WIDTH, HEIGHT))
        py.display.set_caption(TITLE)

        self.clock = py.time.Clock()

        self.new()

    def load_data(self):
        self.tile_sprites = py.sprite.Group()
        self.ui_sprites = py.sprite.Group()

        self.grid = Grid(self, LEVELS[self.level_number])
        self.textbox = TextBox(self, (10, 10))

    def new(self):
        self.running = True
        self.level_number = 0
        self.load_data()

    def quit(self):
        self.running = False
        exit()

    def event(self):
        for e in py.event.get():
            if e.type == py.QUIT:
                self.quit()
            if e.type == py.KEYDOWN:
                if e.key == py.K_ESCAPE:
                    self.quit()

    def update(self):
        py.display.set_caption(TITLE + " - FPS : {:.3}".format(self.clock.get_fps()))
        self.textbox.set_text("Level : {}".format(self.level_number))
        self.grid.update()

        if self.grid.is_completed():
            self.tile_sprites.empty()
            self.level_number += 1
            keys = LEVELS.keys()
            if self.level_number in keys:
                self.grid = Grid(self, LEVELS[self.level_number])
            else:
                print("You've finished the game!")
                self.new()
            self.grid.change = False

        self.ui_sprites.update()

    def draw(self):
        self.screen.fill(BLUE)

        self.grid.draw(self.screen)
        self.ui_sprites.draw(self.screen)

    def run(self):
        while self.running:
            self.clock.tick(FPS)

            self.event()
            self.update()
            self.draw()

            #  Flip the display
            py.display.flip()

    def start_screen(self):
        pass

if __name__ == '__main__':
    game = Game()
    game.run()
