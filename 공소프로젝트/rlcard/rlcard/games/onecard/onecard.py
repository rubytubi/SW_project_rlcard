import random
from operator import *

global count

# 특수상황
def special(selected,isComputer):
    global count  

    #한 번 더: K를 내면 카드를 한 장 더 낼 수 있고, J를 내면 한 턴을 건너뜀
    if(eq(selected[1],'K') or eq(selected[1],'J')):
        if isComputer:
            turn(players[1],isComputer)
        else:
            
            turn(players[0],isComputer)
            
    #모양 바꾸기: 숫자 7을 내면 원하는 모양으로 카드 변경 가능, 숫자는 유지
    if(eq(selected[1],'7')):
        chshape = '♥♣♠◆'
        
        if isComputer:
            change = random.choice(chshape)
            print("컴퓨터가", change, "로 변경했습니다.")
            put[-1][0] = str(change)
        else:
            change = int(input('♥♣♠◆ 중 변경할 모양을 선택하세요: '))
            print("플레이어가", chshape[change-1], "로 변경했습니다.")
            put[-1][0] = chshape[change-1]
    '''
    put[-1][0]은 가장 최근에 놓인 카드(-1)의 모양부분(shape,num)
    컴퓨터는 랜덤선택되고 플레이어는 직접 선택을 하는데, 배열의 인덱스는 0부터 시작하기 때문에 변경하려는 모양(change)에서 1을 빼준다.

    '''        

def turn(hand, isComputer):

    # 전역 변수 접근
    global put, deck, count
    
    # 이름 정하기
    if isComputer:
        name = "컴퓨터"
    else:
        name = "플레이어"

    # 차례
    print('\n')
    print(name, "의 차례입니다.")
    if not isComputer:
        print("현재 패 >>", hand)
    print("놓여진 카드 >>", put[-1])

    # 공격일 때, 가능한 카드 리스트 반환
    def getAvailable2(hand, last_card):
        global count
        
        available = []
        if(last_card[1]=='2'):
            for card in hand:
                if (card[1] == last_card[1] or card[0] == 'Joker'
                    or (card[0]==last_card[0] and card[1] == 'A')):
                    available.append(card)
        elif(last_card[1]=='A'):
            for card in hand:
                if (card[1] == last_card[1] or card[0] == 'Joker'):
                    available.append(card)
                    
        elif(last_card[0]=='Joker'):
            for card in hand:
                if (card[0] == 'Joker'):
                    available.append(card)
                    
        #다음 턴을 위해 non_attack 상태로 세팅         
        count = 'non_attack'
        return available
    
    '''
      last_card는 가장 최근에 놓인 카드로 공격카드엔 2,A,Joker가 있다.
      2일 때 낼 수 있는 카드는, 숫자가 같거나, 모양이 같거나, 모양이 같은 A, Joker이다.
      A일 때 낼 수 있는 카드는, 숫자가 같거나, Joker이다.
      Joker일 때 낼 수 있는 카드는 Joker뿐이다.

      낼 수 있는 카드를 available배열에 담아 리턴한다

     '''        

    # 가능한 카드 리스트를 반환
    def getAvailable(hand, last_card):
        global count
        available = []
        
        for card in hand:
            if (card[0] == last_card[0]
                or card[1] == last_card[1]
                or card[0] == 'Joker'
                or put[-1][0] == 'Joker'):
                available.append(card)
                
        #공격상황을 대비해 attack으로 세팅        
        count = 'attack'
        return available


    # 가능한 카드
    # 공격 상황(2,A,Joker)
    if(put[-1][1]in ['2','A','colored','black']and eq(count,"non_attack")): #공격 방어에 성공 or 카드를 먹어 non_attack상황으로 바뀌었을 땐, 일반상황처럼 getAvailable 호출
        available = getAvailable(hand, put[-1])
   
    elif(put[-1][1]in ['2','A','colored','black']):
        available = getAvailable2(hand, put[-1])

    # 일반상황        
    else:
        available = getAvailable(hand, put[-1])    
        
    if not isComputer:
        print("낼 수 있는 카드:", available)

    # 낼 수 있는 카드가 있는 경우
    if len(available) > 0:
        if isComputer:
            selected = random.choice(available)
            print("컴퓨터가", selected, "를 냈습니다.")
        else:
            i= int(input("몇 번째 카드를 내시겠습니까?"))
            i -= 1
            selected = available[i]
                
        hand.remove(selected)
        put.append(selected)
        #특수상황인지 판단
        special(selected,isComputer)
        
        
    # 낼 수 있는 카드가 없는 경우
    else:

        #뽑을 수 있는 카드가 없으면 내려둔 카드를 다시 deck으로 사용
        if(len(deck) == 0):            
            print("-----덱 보충-----\n")
            deck = put[0:]
            
        #공격 상황에 따라 먹는 경우
        if(count == 'non_attack' and put[-1][1]== '2'):
            print(name,"가 방어할 카드가 없어 2장 먹습니다.")
            for i in range(1,3):
                hand.append(deck.pop())

        elif(count == 'non_attack' and put[-1][1]== 'A'):
            print(name,"가 방어할 카드가 없어 3장 먹습니다.")
            for i in range(1,4):
                hand.append(deck.pop())

        elif(count == 'non_attack' and put[-1][1]== 'colored'):
            print(name,"가 방어할 카드가 없어 8장 먹습니다.")
            for i in range(1,9):
                hand.append(deck.pop())
                
        elif(count == 'non_attack' and put[-1][1]== 'black'):
            print(name,"가 방어할 카드가 없어 5장 먹습니다.")
            for i in range(1,6):
                hand.append(deck.pop())


        else:
            print(name, "가 낼 수 있는 카드가 없어 먹습니다.")
            hand.append(deck.pop())

        
    #수중에 카드가 없으면 승리
    if len(hand) == 0:
        print(name, "가 이겼습니다!")
        return True

    else:
        return False

deck = []

# num과 shape 정의
shapes = '♥♣♠◆'
nums = []
for i in range(2,11):
    nums.append(str(i))
for c in 'JQKA':
    nums.append(c)

# 덱 만들기
for shape in shapes:
    for num in nums:
        deck.append([shape, num])

deck.append(('Joker', 'black'))
deck.append(('Joker', 'colored'))
random.shuffle(deck)

# 플레이어에게 카드 나누기

player = []
computer = []

for i in range(7):
    player.append(deck.pop())
    computer.append(deck.pop())

# 낸 카드에 하나 올려놓기
put = []
put.append(deck.pop())


# 게임 시작
players = [player, computer]
i = 0
while True:

    # i가 0이 아니면 컴퓨터라고 간주
    if i != 0:
        isComputer = True
    else:
        isComputer = False

    if turn(players[i], isComputer):
        break

    # 차례 조정
    i += 1
    if i >= len(players):
        i -= len(players)