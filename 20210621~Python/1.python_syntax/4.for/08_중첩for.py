#08_중첩for
# 다중 for문 : for문 안에 for문을 포함하고 있는 문장
for y in range(3) : #0-2
    for x in range(5) : #0-4
        print(x, end= " ")
    print()

#  print(x, end= " ") 문장의 수행 횟수는? 15번
# print() 문장의 수행 횟수는? 3번