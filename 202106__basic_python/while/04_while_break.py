# 04_while_break.py

# 무한반복 예제(무한 루프)
# 조건을 True로 만들고 계속 반복
# 반복문을 종료하기 위해  break 문 사용

while True :  # 조건이 무조건 참
    print("반복 수행되는 문장입니다. ")
    answer = input("종료 하려면 x 입력 : ")
    if answer == 'x' :
        break #전체 반복 탈출

print("종료했습니다")