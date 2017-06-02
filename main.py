import pygame as py
from sys import exit
from settings import *
from tile import Tile, Grid


class Game:
    """Main class for the game"""
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode((WIDTH, HEIGHT))
        py.display.set_caption(TITLE)

        self.clock = py.time.Clock()
        self.running = True

        self.load_data()

    def load_data(self):
        self.grid = Grid(GRID_WIDTH, GRID_HEIGHT)

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
        self.grid.update()

    def draw(self):
        self.screen.fill(BLUE)

        self.grid.draw(self.screen)

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
