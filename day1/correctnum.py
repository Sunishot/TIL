import random

num = random.randint(1,20)
count = 4
while True:
    guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(count)))
    print(guess)
    count -= 1
    if num == guess:
        print("축하합니다. {}번만에 숫자를 맞히셨습니다.".format(count))
        break
    elif num > guess:
        print("Up")
    else:
        print("Down")
    if count == 0:
            print("아쉽습니다. 정답은 {}였습니다.".format(num))
            break