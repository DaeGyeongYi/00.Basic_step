# while_ex2

su = int(input('마지막 숫자를 입력 하세요 : '))

i = 0 #초기변수
sum = 0 # 누적 변수

while i <= su :
    if i % 2 == 1 : #홀수인지 확인
        sum += i

    i += 1

print('1부터 ', su, '까지 홀수의 합은 ',sum, '입니다')