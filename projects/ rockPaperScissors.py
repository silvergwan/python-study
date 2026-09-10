# radome 임포트
import random

# 규칙을 딕셔너리로 작성
rules = {"가위": "보", "보": "바위", "바위": "가위"}

# 컴퓨터의 선택지 부여
computer_option = ["가위", "바위", "보"]

# computer_option 배열 안에서 랜덤으로 선택시킴
computer_select = random.choice(computer_option)

# 유저에게 입력받음
user_select = input("가위, 바위, 보 중에 하나를 내세요: ")

# 만약 컴퓨터랑 유저의 선택이 같다면
if computer_select == user_select:
    print("비겼습니다.")
# 만약 rules에서 내 선택이 이기는 상대가 컴퓨터의 선택과 같다면?
elif rules[user_select] == computer_select:
    print("이겼습니다!")
# 아니면
else:
    print("졌습니다...")
