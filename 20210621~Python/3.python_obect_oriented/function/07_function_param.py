# 07_function_param

# 인수(인자) 와 매개변수 정리

# 인수(인자) : argument
# 함수에게 실제로 전달되는 값(호출할때 전달하는 값)
# print("hello") - "hello" => 인자

# 매개변수(parameter)
# 함수를 호출할 때 전단되는 실제 값을 받아 저장하는 변수
# def print(data) :

# 파라미터(매개변수)가 있는 함수 정의
#이름값을 하나 넘겨받아서 해당 이름을 출력하는 함수
def show_name(name) :
    print(name)

# show_name 함수 호출
# show_name() #TypeError: show_name() missing 1 required positional argument: 'name'
show_name('홍길동')
show_name(123) # 매개변수도 인자값의 데이터 형태에 따라 형태가 결정된다