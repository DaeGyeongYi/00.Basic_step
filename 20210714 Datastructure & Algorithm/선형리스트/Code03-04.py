##함수 선언부(클래스 선언부)
def add_data(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen - 1] = friend

def insert_data(position, friend):
    katok.append(None)  # 배열의 길이를 하나 늘림
    kLen = len(katok)

    for i in range(kLen - 1, position, -1):
        katok[i] = katok[i - 1]
        katok[i - 1] = None

    katok[position] = friend


def delete_data(position):
    kLen = len(katok)
    katok[position] = None

    for i in range(position + 1, kLen, 1):
        katok[i - 1] = katok[i]
        katok[i] = None
    del (katok[kLen - 1])

##전역 변수부
katok = []
select = -1 #1추가 2삽입 3삭제 4종료

##메인코드부
while (select !=4):
    select = int(input('선택 1~4 -->'))

    if (select == 1) :
        data = input("추가할 값을 입력:")
        add_data(data)
        print(katok)

    elif (select==2):
        data, position = map(int, input().split())
        insert_data(position,data)
        print(katok)

    elif (select==3):
        position = int(input("삭제할 값 입력"))
        delete_data(position)
        print(katok)
    elif (select==4):
        print(katok)
    else:
        print("1~4중에 입력하세요")
