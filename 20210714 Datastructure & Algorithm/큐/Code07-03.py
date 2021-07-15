#일반 큐

def is_queue_full():
    global SIZE, queue, front, rear
    if rear != SIZE-1:
        return False
    elif rear == SIZE -1 and front == -1:
        return True
    else:
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]   #front쪽에서부터, 기존 데이터를 한칸 앞의 인덱스로 이동
            queue[i] = None         #기존 데이터가 있던 자리를 NONE으로 비움
        front -= 1                  #다들 한칸 땡겼으니까 front,rear도 맞춰줘야져
        rear -= 1
        return False

def is_queue_empty():
    global SIZE, queue, front, rear
    if front==rear:
        return True
    else:
        return False

def enqueue(data):
    global SIZE, queue, front, rear
    if is_queue_full():
        print("큐 꽉!")
        return
    rear += 1
    queue[rear] = data

def dequeue():
    global SIZE, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

# 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front , rear= -1,-1



## 메인
enqueue('화사'); enqueue('솔라');enqueue('문별')
print('출구<---', queue, '<--입구')
retData = dequeue(); print('다음 손님 : ', retData)
retData = dequeue(); print('다음 손님 : ', retData)
retData = dequeue(); print('다음 손님 : ', retData)
print('출구<---', queue, '<--입구')
retData = dequeue(); print('다음 손님 : ', retData)
# enQueue('휘인'); enQueue('유나')
# print('출구<---', queue, '<--입구')
# enQueue('꼬북이')
# print('출구<---', queue, '<--입구')