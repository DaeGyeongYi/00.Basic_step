# 01_errors.py

# 예외 처리 방법
# try … except 문 사용

# 예외 처리 문 형식
# try:
    # 	( 예외 발생 가능) 문장
# except 예외 유형:
    # 	예외 처리 문장
# else:
    # 	예외 없을 때 수행 문장
# finally:
    # 	예외 유무와 상관 없이 항상 실행되는 문장

print("============에러 확인===============")

#ZeroDivisionError: division by zero
# print(10/0)

#TypeError
# print("나이 : " + 23 + "살") #can only concatenate str (not "int") to str

#NameError
# print(b) #name 'b' is not defined

# ValueError
c=100
# print("%d%" %c) #incomplete format

#SyntaxError
# if x > 10 #invalid syntax
#     print("홍길동")

#IndexError: l
# a=[1,2,3,4]
# print(a[5]) #ist index out of range

#UnboundLocalError
# def add() :
#     a = a+1 #local variable 'a' referenced before assignment
#
# add()

#ModuleNotFoundError
# import mymodule #No module named 'mymodule'

#FileNotFoundError
# f=open("exception.txt","r") #[Errno 2] No such file or directory: 'exception.txt'

#OSError : 파일 경로는 운영체제 권한이기 때문에 운영체제에서 나타난 에러
# 경로명에 \ 사용하면
# 에러 - \\ 두번 사용하면 에러가 나지 않는다
f=open("c:\\PythonStudy\file_t2.txt",'w')