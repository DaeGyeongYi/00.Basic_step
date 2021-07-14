## 함수
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def print_nodes(start):
    current = start
    print(current.data, end=' ')  # 노드1의 값을 출력하고
    while (current.link != None):  # link가 가리키는게 없을때까지
        current = current.link  # current에 링크가 가리키는 값을 저장하고
        print(current.data, end=' ')  # 그것을 출력함

def insert_node(findData, insertData) :
    global memory, head, current, pre

    # 첫노드 앞에 삽입
    if findData == head.data:
        node = Node()
        node.data = insertData
        node.link = head #지금 헤드에 담겨있는 정보를 추가하려는 노드의 링크와 이어줌
        head = node #헤드를 추가하려는 노드로 교체
        return
    #중간에 있는 노드 앞에 삽입
    current = head #현재 가리키는 노드가 head라고 가정하고 탐색해나갈것
    while current.link !=None: #현재가리키는 노드의 링크가 아무것도 가리키지 않을때까지
        pre = current #이전 노드에 current의 정보들을 담아둠
        current = current.link # 현재 노드는 다음노드를 담아둠
        # 한칸씩 옆으로 가고있다는 것이죵

        if current.data == findData: # 만약 찾는 노드의 위치가 현재 노드라면
            node = Node()            # 새로운 노드생성
            node.data = insertData   # 생성한 노드에 데이터 저장
            node.link = current      # 생성한 노드의 링크를 현재 노드와 이어줌
            pre.link = node          # 이전 노드의 링크를 현재 노드와 이어줌
                                     # 결국 current 앞에 새로운 노드가 삽입됨
            return

    # 마지막 노드에 추가할 때 => 위의 모든 조건을 다 충족하지 못해서 끝까지 왔다면
    node = Node()           #노드 생성
    node.data = insertData  #생성한 노드에 데이터 저장
    current.link = node     #현재 노드의 링크가 생성한 노드를 가리키게함
    return

def delete_node(deleteData):
    global memory, head, current, pre
    #첫 노드 삭제
    if head.data == deleteData: #헤드에 담긴 정보가 삭제할 데이터와 같다면
        current = head          #current에 head의 정보를 담아놓고
        head = head.link        #head는 head의 링크가 가리키는 정보 즉 그다음 노드를 담음
        del current             #이제 기존의 head 삭제
        return
    #그 외 노드 삭제
    current = head              #현재 가리키는 노드는 헤드
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link #이전 노드의 링크와 현재노드의 링크가 가리키는 다음노드를 연결
            del current             # 현재노드는 삭제
            return



## 전역

memory = []

head, current, pre = None,None,None
data_array = ['다현', '정연', '쯔위', '사나', '지효']


## 메인
#첫 노드 생성
node = Node()
node.data = data_array[0]
head = node #헤드로 지정함

memory.append(node) #메모리에 추가

for data in data_array[1:]: #첫노드를 제외하고 끝까지
    pre = node #이전 노드를 반복문 안에 저장(맨처음에는 head를 가리키는중)
    node = Node() #노드를 초기화 함
    node.data = data # 노드에 현재 반복문에서 가져온 현재 데이터를저장함
    pre.link = node #직전 노드의 링크를 현재 노드와 이어줌
    memory.append(node) #메모리에 추가.

print_nodes(head)

