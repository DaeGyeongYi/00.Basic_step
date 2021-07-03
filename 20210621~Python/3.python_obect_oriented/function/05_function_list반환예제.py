# 05_function_list반환예제

# 리스트 반환
# 함수명 :  get_names()
# 함수 기능 : 사용자로부터 3명의 회원 이름을 입력받아 리스트에 추가한 후
# 리스트를 반환하는 함수

# 함수 정의
def get_names() :
    names = []

    for i in range(3) :
        name = input('이름 입력 : ')
        names.append(name)

    return names #리스트 반환

# 함수가 정상 동작 하는지 테스트하는 코드 작성
# get_names()  호출해 회원명단 리스트를 반환받아 저장하고
# 저장된 변수의 값을 출력
name_list = get_names()
print(name_list)
print(type(name_list))