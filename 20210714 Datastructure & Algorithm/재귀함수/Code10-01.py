def openBox():
    global count
    print('박스 열기')
    count -= 1
    if count == 0 :
        print("** 선물 넣기 **")
        return
    openBox()
    print("박스닫기")



#전역
count = 10

#메인
openBox()