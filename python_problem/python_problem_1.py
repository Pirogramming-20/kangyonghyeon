'''
#1단계: 변수 num을 아래와 같이 선언하여라.

#2단계: input() 함수를 이용하여 1에서 3사이의 정수를 입력받는 코드를 작성하여라

#3단계  아래의 내용을 만족하도록 코드를 작성하여라.
 
- 2단계에서 정수를 입력하지 않는 경우, `정수를 입력하세요`를 출력한다.
- 2단계에서 1,2,3을 입력하지 않는 경우, `1,2,3 중 하나를 입력하세요`를 출력한다.
- 올바른 값이 입력될 때까지 입력을 요구한다
.
#4단계: 변수 `num` 을 이용하여, 2단계에서 입력한 수만큼 숫자를 출력하는 코드를 작성하여라.
 예를 들어, 2단계에서 playerA가 3을 입력했다면, 1,2,3을 아래와 같은 형식으로 출력하여라.

#5단계:  아래의 내용이 만족하도록 코드를 작성하여라.
- 1에서 3사이의 정수를 입력받는 코드를 작성하여라.
`부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :`    
- 정수를 입력하지 않는 경우, `정수를 입력하세요`를 출력한다.
- 1,2,3을 입력하지 않는 경우, `1,2,3 중 하나를 입력하세요`를 출력한다.
- 올바른 값이 입력될 때까지 입력을 요구한다.
- 변수 `num`을 이용하여 입력한 수만큼 숫자를 출력하는 코드를 작성하여라.
- 예를 들어, 2단계에서 playerA가 3을 입력한 상태에서, playerB가 2를 입력하면 4,5를 아래와 같은 형식으로 출력하여라.

6단계:  배스킨라빈스31 게임은 참여자가 번갈아가며 숫자를 부른다. 게임이 끝날 때까지 playerA와 playerB에게 번갈아가며 부를 숫자의 개수를 입력받는 코드를 작성하여라.

7단계: 게임이 끝났을 때, 누가 이겼는지 화면에 출력하여라.

8단계: 6단계까지 중복되는 코드를 찾아 함수로 만들어라. 이때, 함수 이름은 brGame으로 한다.

9단계: computer와 대결하는 배스킨라빈스31 게임을 만들어보자. 아래의 내용을 만족하도록 코드를 작성하여라.
'''
import random
def brGame():
    num = 0
    current_player = "computer"

    while num <= 30:
        try:
            if current_player=="computer":
                x=random.randint(1,3)
            else:
                x = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
                if x < 1 or x > 3:
                    print('1, 2, 3 중 하나를 입력하세요')
                    continue
        except ValueError:
            print('정수를 입력하세요')
            continue

        for i in range(num + 1, num + x + 1):
            print(f'{current_player} :', i)
            if i == 31:
                if current_player =="computer":
                    winner="player"
                else:
                    winner="computer"
                print(f'{winner} win!')
                return

        num += x
        if current_player == "computer":
            current_player = "player" 
        else:
            current_player="computer"

brGame()
