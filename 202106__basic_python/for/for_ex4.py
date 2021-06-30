# 카운트 다운 프로그램
count = int(input('시작 숫자를 입력하시오 : '))

for x in range(count, 0, -1) :
    print(x, end=" ")
print("발사")