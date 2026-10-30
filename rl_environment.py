from chess_engine import GameState


class ChessEnvironment:
    def __init__(self):
        self.game_state = GameState()

    def reset(self):
        self.game_state = GameState()
        return self.game_state

    def step(self, origin, target, promotion = 'Q'):
        if self.game_state.game_over:
            raise ValueError("The game is over. Call reset() first.")

        if promotion not in ("Q", "R", "B", "N"):
            raise ValueError("Promotion must be Q, R, B, or N.")

        legal_moves = self.game_state.move.get_valid_moves()

        if (origin, target) not in legal_moves:
            raise ValueError("That move is not legal.")

        result = self.game_state.move.handle_piece_move(origin, target)

        if result == "promotion_pending":
            self.game_state.move.executor.handle_pawn_promotion(promotion)

        return self.game_state