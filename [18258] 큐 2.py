import collections

deq = collections.deque()

N = int(input())

for _ in range(N):
    temp = input().split()
    
    if temp[0] == 'push':
        deq.append(temp[1])
        
    elif temp[0] == 'pop':
        if not deq:
            print(-1)
        else:
            print(deq.popleft())
            
    elif temp[0] == 'size':
        print(len(deq))
            
    elif temp[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
            
    elif temp[0] == 'front':
        if not deq:
            print(-1)
        else:
            print(deq[0])
            
    elif temp[0] == 'back':
        if not deq:
            print(-1)
        else:
            print(deq[-1])
