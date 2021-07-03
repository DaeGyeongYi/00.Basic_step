# 11_function_param_list.py

# 함수에 리스트 전달하는 예제

#함수 이름 :  show_names(names) :
#함수 기능 : 전달받은 변수의 값을 반복문을 활용해서 요소값으로 출력하시오
# 리스트가 전달된다고 가정
def show_names(names) :
    for name in names :
        print(name, end = ' ')

#함수 테스트
#리스트를 인수로 전달한 후 출력이 일어나는지 확인
names_list=['Kim','Lee','Park']
show_names(names_list)