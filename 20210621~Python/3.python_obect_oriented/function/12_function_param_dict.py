# 12_function_param_dict.py

# 함수에 딕셔너리 전달하는 예제
#함수 이름 :  show_info(info) :
#함수 기능 : 전달받은 변수의 값을 반복문을 활용해서 요소값으로 출력하시오
# 딕셔너리가 전달된다고 가정
def show_info(info) :
     print(info) #dict 전체 출력
     print('이름 : ' + info['name']) #name 키의  value 출력
     print('연락처 : ' + info['phone'])

#함수 테스트
# 호출시 딕셔너리를 인수로 전달한 후 출력 확인
info_list = {'name':'Kim','age':23, 'phone':'010-1234-1234'}
show_info(info_list)