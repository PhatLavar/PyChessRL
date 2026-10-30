import random


class RandomAgent:
    def choose_action(self, legal_actions):
        if not legal_actions:
            raise ValueError("There are no legal actions to choose from.")
        return random.choice(legal_actions)