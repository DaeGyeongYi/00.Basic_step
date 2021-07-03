# 10_function_default_param2.py

# 디폴트 매개변수를 2개 사용
def show_info(name,year=4, age=23) :
    print(name, year, age)

show_info("홍길동")
show_info("홍길동",3)
show_info("홍길동",1,20)