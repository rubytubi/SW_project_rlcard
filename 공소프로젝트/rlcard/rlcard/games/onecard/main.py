from onecard import OnecardGame, Player

def main():
    # 플레이어 생성
    player1 = Player(0, False)
    player2 = Player(1, True)

    # 게임 생성
    game = OnecardGame()
    game.players = [player1, player2]

    # 게임 시작
    state = game.init_game()

    while True:
        # 현재 플레이어의 행동 받기
        current_player = game.players[state['current_player']]
        action = current_player.play(state)

        # 행동 적용
        next_state, scores = game.step(action)

        # 게임 종료 확인
        if scores is not None:
            print(f'Game over, scores: {scores}')
            break
        else:
            state = next_state

if __name__ == "__main__":
    main()
