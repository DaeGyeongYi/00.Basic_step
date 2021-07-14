stack = [None,None,None,None,None]
top = -1

top +=1
stack[top] ='녹차'
top+= 1
stack[top] = '꿀물'

print('바닥:',stack)

data = stack[top]
stack[top] =None
top -= 1
print("팝 --->", data)

data = stack[top]
stack[top] = None
top -= 1
print('팝--->',data)
