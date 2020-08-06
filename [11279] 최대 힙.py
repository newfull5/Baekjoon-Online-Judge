import heapq
from sys import stdin

heap = []

n = int(stdin.readline())

for _ in range(n):
    temp = int(stdin.readline())
    
    if temp == 0:
        if not heap:
            print(0)
        else:
            print(-1*(heapq.heappop(heap)))
    else:
        heapq.heappush(heap,-temp)

        
