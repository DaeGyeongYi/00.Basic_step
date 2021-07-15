#원형큐

def is_queue_full():
    global SIZE, queue, front, rear
    if (rear+1) % SIZE == front:
        return True
    else:
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
    rear = (rear+1)%SIZE
    queue[rear] = data

def dequeue():
    global SIZE, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다")
        return None
    front = (front+1)%SIZE
    data = queue[front]
    queue[front] = None
    return data

# 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front , rear= 0,0



## 메인
enqueue('화사'); enqueue('솔라');enqueue('문별')
enqueue('휘인'); enqueue('유나')
print('출구<---', queue, '<--입구')

retData = dequeue(); print('다음 손님 : ', retData)
print('출구<---', queue, '<--입구')
retData = dequeue(); print('다음 손님 : ', retData)
print('출구<---', queue, '<--입구')
enqueue('재남'); enqueue('꼬복이')
print('출구<---', queue, '<--입구')
#
# retData = deQueue(); print('다음 손님 : ', retData)
# retData = deQueue(); print('다음 손님 : ', retData)
# print('출구<---', queue, '<--입구')
# enQueue('재남')
# print('출구<---', queue, '<--입구')
# enQueue('선미')
# print('출구<---', queue, '<--입구')
# enQueue('ㅋㅋ')
# print('출구<---', queue, '<--입구')
#
#
# retData = deQueue(); print('다음 손님 : ', retData)
# print('출구<---', queue, '<--입구')
# retData = deQueue(); print('다음 손님 : ', retData)
# enQueue('휘인'); enQueue('유나')
# print('출구<---', queue, '<--입구')
# enQueue('꼬북이')
# print('출구<---', queue, '<--입구')