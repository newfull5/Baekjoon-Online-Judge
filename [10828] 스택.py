import sys

t = int(sys.stdin.readline())

stack = []

for _ in range(t):
    inputs = sys.stdin.readline()
    
    if 'push' in inputs:
        stack.append(int(inputs.split()[-1]))
    if 'top' in inputs:
        if not stack:
            print('-1')
        else:
            print(stack[-1])
    if 'size' in inputs:
        print(len(stack))
        
    if 'empty' in inputs:
        if not stack:
            print(1)
        else:
            print(0)
            
    if 'pop' in inputs:
        if not stack:
            print(-1)
        else:
            print(stack.pop())
        
