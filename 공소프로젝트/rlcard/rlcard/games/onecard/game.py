import random
from rlcard.games.onecard.judger import Judger

from rlcard.games.onecard.round import Round

class OnecardGame:
    def __init__(self):
        self.players = []
        self.judger = Judger()
        self.round = None
        self.scores = None

    def init_game(self):
        self.round = Round(self.players)
        self.scores = [0, 0]
        return self.round.start_new_round(self.scores)

    def step(self, action):
        is_over, next_player_id = self.round.step(action)
        if is_over:
            scores = self.judger.judge(self.round)
            self.round = Round(self.players)
            return self.round.start_new_round(scores), scores
        else:
            return self.round.get_state(next_player_id), None
