su = int(input('마지막 숫자를 입력하세요: '))

i = 0
sum = 0
while  i <= su :
    if i % 2 == 1 :
        sum += i
    i += 1

print('1부터 ', su , '까지의 홀수의 합은 ', sum, '입니다.')
