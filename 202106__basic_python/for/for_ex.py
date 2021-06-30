# 1에서 20 수 중에서 3의 배수만 출력
for x in range(1, 21) :
    if x % 3 == 0 :
        print(x, end=" ")
print()
for x in range(3,21,3) :
    print(x, end=" ")