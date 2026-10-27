from chess_engine import GameState


class ChessEnvironment:
    def __init__(self):
        self.state = GameState()

    def reset(self):
        self.state = GameState()
        return self.state