s_id = "flower"
s_pass = "1234"

u_id = input("아이디 입력 : ")
u_pass = input("비밀번호 입력 : ")

if ((s_id==u_id) and (s_pass==u_pass)) :
    print("로그인 성공!")
else :
    print("로그인 실패!")

