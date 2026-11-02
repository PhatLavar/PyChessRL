import torch

PIECES = (
    "wP", "wN", "wB", "wR", "wQ", "wK",
    "bP", "bN", "bB", "bR", "bQ", "bK",
)


def encode_board(board):
    encoded = torch.zeros((12, 8, 8), dtype=torch.float32)

    for row_index, row in enumerate(board):
        for column_index, piece in enumerate(row):
            if piece == "--":
                continue

            plane = PIECES.index(piece)
            encoded[plane, row_index, column_index] = 1.0

    return encoded
