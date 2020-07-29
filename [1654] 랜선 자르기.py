a, b = map(int, input().split())

stack = []
for _ in range(a):
    stack.append(int(input()))
    
left, right = 1, max(stack)

while left<=right:
    mid = (left+right)//2
    
    temp = sum(map(lambda x: x//mid, stack))
    if temp >= b:
        left= mid+1
    elif temp < b:
        right = mid-1
        
print(right)
