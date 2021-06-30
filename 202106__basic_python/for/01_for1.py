# 01_for1
# for 문 : 정해진 횟수만큼 반복할 때 주로 사용
# 문법
# for 반복요소를 저장할 변수 in 반복을위한 리스트 또는 범위 :
#   반복문장1
#   반복문장2...

# 리스트 [''홍길동','이몽룡','성춘향','변학도']의 요소를 모두 출력하시오
s_name = ['홍길동','이몽룡','성춘향','변학도'] #리스트 생성
# print(s_name[0])
# print(s_name[1])
# print(s_name[2])
# print(s_name[3])

for name in s_name :
    print(name)

num = [1,2,3,4,5,6,7,8,9]
# 위 리스트의 요소들을 각각 출력하시오
for n in num :
    print(n)
# 위 리스트의 요소들을  한 라인에  출력하시오
print("=====================================")
for n in num :
    print(n, end=' ')

# for num in num :
#     print(num)


#============================================
# 반복 범위 설정 : range() 함수
# 특정 범위의 정수 생성
# range(start, stop, step)

# range(10)# start,step 생략 10개의 정수 0~9까지의 정수(시작은 0)
# range(1,10) # step 생략 1에서 9까지의 정수 - start에서 stop-1 까지의 정수
# range(1,10,2) #start  에서 stop-1까지  step  간격으로 정수 생성 - 1에서 9까지 2씩 건너뛰면서

print()
print("==================================")

# range(10)# start,step 생략 10개의 정수 0~9까지의 정수(시작은 0)
for i in range(10) : # 0~ 9
    print(i)
print('====')
# range(1,10) # step 생략 1에서 9까지의 정수 - start에서 stop-1 까지의 정수
for i in range(1,10) :
    print(i)
print('====')
# # range(1,10,2) #start  에서 stop-1까지  step  간격으로 정수 생성 - 1에서 9까지 2씩 건너뛰면서
# for i in range(1,10,2) :
#     print(i)
#
# for i in range(11,21) : # 11~20
#     print(i)
#
for i in range(10,1,-1) :
    print(i)

