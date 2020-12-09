N = int(input())

import heapq

heap = list(map(int, input().split()))

for _ in range(N-1):
    heap += list(map(int, input().split()))
    heapq.heapify(heap)
    
    for __ in range(N):
        heapq.heappop(heap)

print(heapq.heappop(heap))
