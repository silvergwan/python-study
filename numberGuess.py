# 랜덤 숫자를 뽑기 위해 random 모듈 import
import random

# 랜덤 숫자는 1부터 100사이의 정수형 난수
randNum = random.randrange(1, 101)

# 1은 정수라서 참, 그래서 무한반복
while 1:
    # 사용자에게 숫자를 입력 받음
    userNum = int(input("숫자를 입력하세요 : "))
    # 만약 랜덤 숫자가 사용자에게 입력받은 숫자보다 크면 "더 큽니다."
    if randNum > userNum:
        print("더 큽니다.")
    # 만약 랜덤 숫자가 사용자에게 입력받은 숫자보다 작으면 "더 작습니다."
    elif randNum < userNum:
        print("더 작습니다.")
    # 만약 랜덤 숫자가 사용자에게 입력받은 숫자와 같다면 "정답입니다!" 출력 후 break로 while문을 빠져나감
    else:
        print("정답입니다!")
        break
