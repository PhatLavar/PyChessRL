import pygame as pg

from chess_engine import GameState
from chess_ui.config import FPS, WINDOW_SIZE
from chess_ui.renderers import BoardRenderer


class ChessGame:
    """Display the initial board in the PyChessRL window."""

    def __init__(self):
        self.game_state = GameState()

    def run(self):
        pg.init()
        try:
            screen = pg.display.set_mode(WINDOW_SIZE)
            pg.display.set_caption('PyChessRL')
            renderer = BoardRenderer(self.game_state)
            clock = pg.time.Clock()
            running = True
            while running:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False
                    elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                        running = False
                if running:
                    renderer.draw(screen)
                    pg.display.flip()
                    clock.tick(FPS)
        finally:
            pg.quit()
