"""
#2020.07.29
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
"""
#2020.12.11
a,b = map(int, input().split())

arr = []
for _ in range(a):
    arr.append(int(input()))


left, right = 1, max(arr)

while left<=right:
    
    mid = (left + right)//2
    
    answer = sum(map(lambda x: x//mid, arr))
    
    if answer >= b:
        left = mid + 1
    else:
        right = mid -1
        
print(right)
