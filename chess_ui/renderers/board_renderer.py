import pygame as pg

from chess_engine import Piece
from chess_engine.utilities import EMP
from chess_ui.config import (
    BOARD_DIMENSION, BOARD_PIXEL_SIZE, BOARD_LIGHT_COLOR, BOARD_DARK_COLOR,
    SQUARE_SIZE, PIECE_IMAGE_DIRECTORY, SIDEBAR_COLOR, TEXT_COLOR,
    MUTED_TEXT_COLOR,
)


class BoardRenderer:
    """Render engine state without changing it; reserve the right side for the arena."""

    def __init__(self, game_state):
        self.game_state = game_state
        self.piece_images = {
            piece: pg.transform.smoothscale(
                pg.image.load(str(PIECE_IMAGE_DIRECTORY / f'{piece}.png')).convert_alpha(),
                (SQUARE_SIZE, SQUARE_SIZE),
            )
            for piece in Piece.PIECES
        }
        self.title_font = pg.font.Font(None, 36)
        self.body_font = pg.font.Font(None, 23)

    def draw(self, screen):
        screen.fill(SIDEBAR_COLOR)
        colors = (BOARD_LIGHT_COLOR, BOARD_DARK_COLOR)
        for row in range(BOARD_DIMENSION):
            for col in range(BOARD_DIMENSION):
                rect = pg.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pg.draw.rect(screen, colors[(row + col) % 2], rect)
                piece = self.game_state.board.get_piece((row, col))
                if piece != EMP:
                    screen.blit(self.piece_images[piece], rect)

        x = BOARD_PIXEL_SIZE + 24
        screen.blit(self.title_font.render('PyChessRL', True, TEXT_COLOR), (x, 28))
        screen.blit(self.body_font.render('Board preview', True, MUTED_TEXT_COLOR), (x, 72))
        screen.blit(self.body_font.render('Esc to close', True, MUTED_TEXT_COLOR), (x, BOARD_PIXEL_SIZE - 40))
