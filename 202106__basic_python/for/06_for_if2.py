# 06_for_if2
# 정수  10개를 사용자로부터 입력받아서 양, 음, 0의 개수 출력하는 프로그램

# 입력양식
# 숫자 1 입력 : -1
# 숫자 2 입력 : 9
# ...
# 숫자 10 입력 : 5

pos=neg=zero = 0
for i in range(1, 11) :
    n = int(input("숫자" + str(i )+ '입력 : '))

    if n > 0 :
        pos += 1
    elif n < 0 :
        neg += 1
    else :
        zero += 1

print("---------------------------------")
print("양의 개수 : ", pos)
print("음의 개수 : ", neg)
print("0의 개수 : ", zero)