#isalph_ex.py

# count 누적변수 초기화
alphas=digits=spaces=others=0

# 문장을 입력받는 코드
string = input("문장을 입력하세요 : ")

# 입력된 문장을 하나씩 추출해서 판단하는 코드
for c in string :
    # print(c) #c 변수에 한 문자씩 대입
    if c.isalpha() : #c.isalpha()== True
        alphas = alphas + 1
    elif c.isdigit() :
        digits += 1
    elif c.isspace() :
        spaces += 1
    else :
        others += 1

print("문자 : %d 개" %alphas)
print('숫자 : %d 개' %digits)
print('공백 : %d 개' % spaces)
print('기타 : %d개' % others)