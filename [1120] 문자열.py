a, b = input().split()
length = len(b) - len(a)
stack = []

for i in range(0,length+1):
    stack.append('@'*i + a + '@'*(length-i))
    
answer = 50000000
for array in stack:
    cnt = 0
    for i in range(0, len(b)):
        if array[i] != b[i]:
            cnt += 1
            
    if answer > cnt-length:
        answer = cnt-length
        
        
print(answer)
