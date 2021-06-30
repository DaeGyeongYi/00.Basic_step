# 07_for_명단확인
# 사용자가 입력한 이름이 명단리스트에 있는지 검색 후 결과를 출력

# 입력양식 :
# 이름 입력 : 홍길동

#출력양식 :
# 명단에 있습니다 또는 명단에 없습니다

namelist = ["홍길동","이몽룡","성춘향","변학도"]

# 이름 입력
search_name = input('이름입력 : ')

for name in namelist :
    if search_name == name : #명단에서 이름을 찾은 경우 - 반복 중단
        find = True
        break #반복 탈출 제어코드
    else : # 명단에서 못찾은 경우 - 반복 끝까지 계속
        find = False

# print(find)
if find : #if find == True :
    print('명단에 있습니다')
else :
    print('명단에 없습니다')

# if True :
#     print(5)