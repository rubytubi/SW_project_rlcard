import random


class Round:
    def __init__(self, players):
        self.deck = []
        self.players = players
        self.current_player = 0
        self.shpae_changer = False
        self.attack_count = 0

    def start_new_round(self, scores):
        self.init_deck()
        self.distribute_cards()
        self.current_player = 0
        self.shpae_changed = False
        self.scores = scores
        self.attack_count = 0
        return self.get_state(self.current_player)
    
    def special_case(self, card):
        if card[1] == '2':
            self.attack_count += 2
        elif card[1] == 'A':
            self.attack_count += 3
        elif card[1] == '7':
            self.shape_changed = True
        elif card[1] == 'J':
            self.current_player = (self.current_player - 1) % 2 # 'J' 카드 효과: 차례를 한 번 더 가짐
        elif card[1] == 'Joker':
            if card[0] == 'black':
                self.attack_count += 5
            else: # colored Joker
                self.attack_count += 8

    def init_deck(self):
        # 덱 초기화
        shapes = '♥♣♠◆'
        nums = [str(i) for i in range(2, 11)] + list('JQKA')
        for shape in shapes:
            for num in nums:
                self.deck.append([shape, num])
        self.deck.append(['Joker', 'black'])
        self.deck.append(['Joker', 'colored'])
        random.shuffle(self.deck)

    def distribute_cards(self):
        # 카드 배분
        for i in range(7):
            self.players[0].hand.append(self.deck.pop())
            self.players[1].hand.append(self.deck.pop())

    def get_state(self, player_id):
        # 상태 반환
        return {'hand': self.players[player_id].hand, 'current_card': self.deck[-1], 'scores': self.scores}
    
    def change_shape(self, shape):
        self.deck[-1][0] = shape
        self.shape_changed = False

    def step(self, action):
        # 플레이어의 행동 처리
        self.players[self.current_player].hand.remove(action)
        self.deck.append(action)
        self.special_case(action) # 특수 카드 처리

        if len(self.players[self.current_player].hand) == 0:
            return True, self.current_player
        else:
            self.current_player = (self.current_player + 1) % 2
            if self.attack_count > 0: # 공격 상황 처리
                for _ in range(self.attack_count):
                    if len(self.deck) > 0:
                        self.players[self.current_player].hand.append(self.deck.pop(0))
                self.attack_count = 0
            if self.shape_changed: # '7' 카드 효과 처리
                return 'change_shape', self.current_player
            return False, self.current_player
