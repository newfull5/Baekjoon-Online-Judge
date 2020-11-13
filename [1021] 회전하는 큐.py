def RotateLeft(arr):
    arr.append(arr.popleft())

def RotateRight(arr):
    arr.appendleft(arr.pop())

import collections

a,b = map(int, input().split())

answer = list(map(int, input().split()))

answer.reverse()

arr = collections.deque(list(range(1,a+1)))

cnt = 0

for _ in range(b):
    
    index_ = arr.index(answer.pop())
    
    if index_ - 0 < len(arr) - index_:
        for __ in range(index_-0):
            RotateLeft(arr)
            cnt += 1
        arr.popleft()

    elif index_ - 0 >= len(arr) - index_:
        for __ in range(len(arr) - index_):
            RotateRight(arr)
            cnt += 1
        arr.popleft()
        
print(cnt)    
