# function_return_ex2.py

# 함수 이름 : get_area()
# 사각형의 가로길이와 세로길이를 입력 받아 면적을 구하여 반환 하는 함수
def get_area() :
    width = int(input("가로길이 입력 : "))
    height = int(input("세로길이 입력 : "))
    # 사각형 면적 계산
    area = width * height
    return area # 결과값 반환 :  return width * height

#테스트코드에서 함수 호출해서 값을 반환받아 출력
rect_area = get_area()
print("사각형의 면적 : %d" % rect_area)
