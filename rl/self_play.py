from rl.rl_environment import ChessEnvironment
from rl.random_agent import RandomAgent

def play_game(max_plies=256):
    if max_plies < 1:
        raise ValueError("max_plies must be at least 1.")

    env = ChessEnvironment()
    white_agent = RandomAgent()
    black_agent = RandomAgent()

    plies = 0

    while not env.game_state.game_over and plies < max_plies:
        if env.game_state.white_to_move:
            agent = white_agent
        else:
            agent = black_agent

        action = agent.choose_action(env.legal_actions())
        origin, target, promotion = action

        env.step(origin, target, promotion)
        plies += 1

    return {
        "plies": plies,
        "terminated": env.game_state.game_over,
        "truncated": not env.game_state.game_over,
        "reason": env.game_state.game_result or "move_limit",
        "winner": env.game_state.winner,
        "rewards": env.terminal_rewards(),
    }

if __name__ == "__main__":
    print(play_game())