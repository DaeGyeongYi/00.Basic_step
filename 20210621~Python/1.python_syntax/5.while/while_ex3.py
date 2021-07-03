
while True :
    s = input('숫자(정수)만 입력하세요. 종료를 원하면 x를 입력하세요 : ')

    if s == 'x' :
        print('종료합니다')
        break
    if int(s) %2 == 0 :
        continue

    print(s+'는 홀 수 입니다.')