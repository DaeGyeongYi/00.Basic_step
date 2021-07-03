# 14_function_kwargs.py

#가변길이 매개변수 **kwargs
# keyword arguments의 약자,  key=value 형태로 값을 받는다

def show_keywards(**kwargs) : #인수는 dict 형태로 전달 된다
    print(kwargs)
    print(type(kwargs))


# 함수 호출
show_keywards() #빈 dict가 전달된다
show_keywards(a=3)

show_keywards(id='sun',
                        name='kim',
                        phone='010-1234-1234')

show_keywards(num=3,
                        val='kim',
                        str='abcdef')