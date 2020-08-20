cnt = 0

for _ in range(int(input())):
    string = list(input())
    
    stack = ['-1']
    
    for char in string:
        if stack[-1] != char:
            stack.append(char)
            
    if len(stack) == len(set(stack)):
        cnt += 1
        
print(cnt)
