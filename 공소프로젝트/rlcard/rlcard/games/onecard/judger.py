class Judger:
    def judge(self, round):
        if len(round.players[0].hand) == 0:
            return [1, -1]
        elif len(round.players[1].hand) == 0:
            return [-1, 1]
        else:
            return [0, 0]