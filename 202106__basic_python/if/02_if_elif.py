# 02_if_elif
# 또 다른 조건이 있을 때  elif로 조건 추가 가능
# if (조건식1) :
    #조건식1이 참일경우 수행되는 문장
# elif(조건식2) :
    #조건식2가 참일경우 수행되는 문장
# elif(조건식n) :
    #조건식 n이 참일경우 수행되는 문장
# else :
#   모든 조건식이 거짓일 경우 수행되는 문장

num = int(input("정수 입력 : "))

if num < 0 :
    print("음수")
elif num > 0 :
    print("양수")
else :
    print("0")

