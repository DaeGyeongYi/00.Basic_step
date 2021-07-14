## 함수, 클래스 선언부
class Node() : # 내가 지어준 이름
    def __init__ (self) :
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    print(current.data, end='  ')
    while current.link != None:
        current = current.link
        print(current.data, end='  ')
    print()

def add_node(addData) :  # 노드 추가하기 (마지막에 넣기)
    global memory, head, current, pre
    if len(memory) == 0 : # 노드가 하나도 없다면 (= 첫 노드면)
        node = Node()
        node.data = addData
        head = node
        memory.append(node)
    else : # 기존에 노드가 있다면. 제일 마지막으로 이동 후에 추가
        current = head
        while current.link != None :
            current = current.link #이동 끝
        pre = current
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

def insert_node(findData, insertData) :
    global memory, head, current, pre
    # 예) 다현 앞에 화사를 삽입
    if head.data == findData : # 첫 노드 앞에 삽입
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    current = head                 # 중간 노드 삽입
    while  current.link != None :
        pre = current
        current = current.link
        if current.data == findData :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    node = Node()    #  마지막에 노드 삽입
    node.data = insertData
    current.link = node

def delete_node(deleteData) :
    global memory, head, current, pre

    if head.data == deleteData : # 첫 노드 삭제
        current = head
        head = head.link
        del(current)
        return

    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == deleteData :
            pre.link = current.link
            del(current)
            return

def findNode(findData) :
	global memory, head, current, pre
	current = head
	if current.data == findData :
		return current
	while current.link != None :
		current = current.link
		if current.data == findData :
			return current
	return Node()	# 빈 노드 반환

## 전역 변수부
memory = []
head, current, pre = None, None, None
select = -1

## 메인 코드 부분 ##
if __name__ == "__main__":

    while (select != 5):

        select = int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 찾기, 5: 종료)--> "))

        if (select == 1):
            data = input("추가할 데이터--> ")
            add_node(data)
            printNodes(head)
        elif (select == 2):
            fData = input("찾을 데이터--> ")
            insData = input("삽입할 데이터--> ")
            insert_node(fData, insData)
            printNodes(head)
        elif (select == 3):
            dData = input("삭제할 데이터--> ")
            delete_node(dData)
            printNodes(head)
        elif (select == 4):
            fData = input("찾을 데이터--> ")
            fNode = findNode(fData)
            print(fNode.data)
        elif (select == 5):
            printNodes(head)
            exit
        else:
            print("1~4 중 하나를 입력하세요.")
            continue