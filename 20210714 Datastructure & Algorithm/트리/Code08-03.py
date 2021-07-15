class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 전역변수
memory = []
root = None

#실무에서는 name_arr 대신 DB내의 대용량 데이터, 크롤링한데이터를 사용
import random
name_arr = [random.randint(100000,9999999) for _ in range(500)]
#name_arr.insert(250, 1234)
print(name_arr)
## 메인코드
# 첫 노드(=루트) 만들기
node = TreeNode()
node.data = name_arr[0]
root = node
memory.append(node)


#나머지 노드를 자리잡기
for name in name_arr[1:]:
    node =TreeNode()
    node.data = name

    current = root
    while True:
        if name < current.data : # 작은게 왼쪽으로 정렬
            if current.left == None: #비어있어?
                current.left = node #그렇다면 그곳에 이 node를 저장
                break
            current = current.left #아니라면 지금노드를 기준으로 다시 while문 반복
        else:                    #더 크다면
            if current.right == None:  #비어있어?
                current.right = node   # 그렇다면 그곳에 저장
                break
            current= current.right    # 아니라면 지금 노드를 기준으로 다시 while문 반복

    memory.append(node) #while문이 끝났으니 memory에 저장

print("이진 탐색 트리 구성 완료")
findData = 1234

current = root
while True:
    if current.data == findData:
        print(findData, "찾음")
        break
    elif findData < current.data:
        if current.left == None:
            print(findData, '없어요')
            break
        current = current.left

    else:
        if current.right == None:
            print(findData, '없어요ㅠㅠ')
            break
        current = current.right