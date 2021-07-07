# 03_exception2.py

#  else 문 수행 - 예외가 발생하지 않은 경우

# try :
#     num = int(input("숫자 입력 : "))
#     # print(num)
# except ValueError :
#     print("숫자가 아닙니다")
# else :  # 에러가 없는 경우 실행
#     print(num)

# 오류 발생 시 아무것도 하지 않고 넘어가기
# try :
#     num = int(input("숫자 입력 : "))
#     print(num)
# except ValueError :
#     pass
#
# print('종료')

##finally 구문
try :
    num = int(input("숫자 입력 : "))
except ValueError :
    print("숫자가 아닙니다")
else :  # 에러가 없는 경우 실행
    print(num)
finally:
    print("종료")

