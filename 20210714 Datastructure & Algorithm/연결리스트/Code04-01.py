class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

node1 = Node()
node1.data = '다현'

node2 = Node()
node2.data = '정연'
node1.link = node2

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5



current = node1 # 노드 1에서출발하고
print(current.data, end = ' ') #노드1의 값을 출력하고
while (current.link !=None): # link가 가리키는게 없을때까지
    current = current.link  #current에 링크가 가리키는 값을 저장하고
    print(current.data, end=' ')# 그것을 출력함

# 연결리스트 사이에 새 노드를 삽입하기
new_node = Node()
new_node.data= '재남'
new_node.link = node2.link
node2.link = new_node

#연결리스트 내부의 노드 삭제
node2.link = node3.link
del(node3)