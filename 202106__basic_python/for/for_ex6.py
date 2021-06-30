# for_ex6.py

# 첫번째 별 출력
# # 4행 5열 별 출력
# for i in range(1, 5) :  # 4행
#     for j in range(1,6) : # 5열
#         print('*', end='')
#     print()
#     # ** ** *
    # ** ** *
    # ** ** *
    # ** ** *

# 두번째 별 출력
# 5행
# 행번호 만큼의 별이 각 행에 출력
# 1행 별 1개 출력 :  0,1
# 2행 별 2개 출력 : 0, 2
#...
# 5행 별 5개 출력 : 0,5

# for i in range(1, 6) :  # 5행
    # for j in range(0,i) : #
    #     print('*', end='')
    # print()

# 세번째 별 출력
# 5행
# 1행 별 5개 출력 :  0,5
# 2행 별 4개 출력 : 0, 4
#...
# 5행 별 1개 출력 : 0,1

# for i in range(1, 6):  # 5행
#     for j in range(0, 6-i):  # i가 1이면 0-5,  i가 2가되면 0-4
#         print('*', end='')
#     print()

# 네번째 별 출력
for i in range(0,5) :
    # 스페이스 찍기
    for j in range(5-1,i,-1) : #i 의 값 변화 : 0,1,2,3,4
        print(' ', end='')
    # 별 찍기
    for k in range(0,i*2+1):#i 의 값 변화 : 0,1,2,3,4 => 1,3,5,7,9 => i*2+1
        print('*', end='')

    print()

n=6
for i in range(0,n) :
    # 스페이스 찍기
    for j in range(n-1,i,-1) : #i 의 값 변화 : 0,1,2,3,4
        print(' ', end='')
    # 별 찍기
    for k in range(0,i*2+1):#i 의 값 변화 : 0,1,2,3,4 => 1,3,5,7,9 => i*2+1
        print('*', end='')

    print()


# 다섯번째 별


for i in range(0,5) :
    # 스페이스 찍기
    for j in range(0,i) :
        print(' ',end='')
    #별 찍기
    for k in range(9,i*2,-1) :
        print('*',end='')
    print()

# 행을 늘리면 찍히는 별도 늘어나게 수정
n= 7
for i in range(0,n) :
    # 스페이스 찍기
    for j in range(0,i) :
        print(' ',end='')
    #별 찍기
    for k in range(n*2-1,i*2,-1) :
        print('*',end='')
    print()
