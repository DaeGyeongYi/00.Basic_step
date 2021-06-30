# 사용자가 선택한 도형의 필요데이터를 입력받아 면적을 구하는 프로그램

# 사용자가 선택한 도형
choice = input('도형 입력(1: 사각형, 2: 삼각형, 3:원) : ')
shape = "" # 필요변수 생성 후 초기화

# 필요데이터 입력 ( 도형에 따라 다른 데이터 입력 유도)
#면적 계산 (도형에 따라 다른 계산 식 사용)
if choice == "1" : #사각형 선택
    w = int(input("가로 입력 : "))
    h = int(input("세로 입력 :"))
    area = w * h
    shape = "사각형"

elif choice == "2" : #삼각형 선택
    b = int(input("밑변 입력 : "))
    h = int(input("높이 입력 :"))
    area = b * h /2
    shape = "삼각형"

else : # 원 선택
    r = int(input('반지름 입력 : '))
    area = 3.141592 * r * r
    shape = '원'

print('%s의 면적 = %.2f' % (shape, area))
