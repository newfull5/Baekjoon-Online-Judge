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
"""
#2021.07.05
K, N = map(int, input().split())
arr = []

for _ in range(K):
    arr.append(int(input()))
    
left, right = 0, max(arr)

while left <= right:
    
    mid = (left + right) // 2
    
    if mid == 0:
        right = 1
        break

    cnt = sum([l // mid for l in arr])

    if cnt < N:
        right = mid - 1

    elif cnt >= N:
        left = mid + 1
        
print(right)
