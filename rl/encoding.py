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

def encode_castling_rights(game_state):
    rights = game_state.castling_rights

    right_values = (
        rights["w"]["king_side"],
        rights["w"]["queen_side"],
        rights["b"]["king_side"],
        rights["b"]["queen_side"],
    )

    planes = torch.zeros((4, 8, 8), dtype=torch.float32)
    for index, value in enumerate(right_values):
        planes[index] = float(value)

    return planes

def encode_en_passant(game_state):
    plane = torch.zeros((1, 8, 8), dtype=torch.float32)
    target = game_state.en_passant_target

    if target is not None:
        row, column = target
        plane[0, row, column] = 1.0

    return plane

def encode_observation(game_state):
    piece_planes = encode_board(game_state.board.board)
    
    turn_value = float(game_state.white_to_move)
    turn_plane = torch.full(
        (1, 8, 8),
        turn_value,
        dtype=torch.float32,
    )

    castling_planes = encode_castling_rights(game_state)
    en_passant_plane = encode_en_passant(game_state)

    return torch.cat(
        (
            piece_planes,
            turn_plane,
            castling_planes,
            en_passant_plane
        ),
        dim=0,
    )
