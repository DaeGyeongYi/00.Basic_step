# 정수 2개를 입력 받아서 두수 사이의 합을 구하는 프로그램 작성 (for 문 사용)

# 정수 2개 입력 받기
print("숫자 1 이 더 작은 정수를 입력하세요")
num1 = int(input("숫자 1 입력 :  "))
num2 = int(input("숫자 2 입력 : "))

sumx = 0

for x in range(num1, num2+1) :
    sumx += x
print("%d 부터 %d 까지의 합 : %d" % (num1, num2, sumx))