'''
input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = 0

for a,b in zip(sorted(a), sorted(b, reverse=True)):
    answer += a*b
    
print(answer)
'''

input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))

import heapq

heapq.heapify(a)

b = [num*-1 for num in b]

heapq.heapify(b)

answer = 0
while a:
    answer += heapq.heappop(a) * heapq.heappop(b) * -1
    
print(answer)
