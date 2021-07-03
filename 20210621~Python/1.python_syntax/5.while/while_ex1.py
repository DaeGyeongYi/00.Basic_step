# while_ex1

#노래방 기계 : 1곡에 2000 월
# 현재 잔액 : 10,000월

song = 2000
money = 10000
count = 0 # 몇곡을 불렀는지 누적하는 변수

while money != 0 : #money가 0이 아닐때 반복
    count += 1
    money = money - song
    print("노래를 "+str(count) + "곡 불렀습니다.")

    if money == 0 : # money 가 0이면
        print('잔액이 없습니다. 종료 합니다.')
        # break
    else :
        print("현재 " + str(money) + "원 남았습니다. ")