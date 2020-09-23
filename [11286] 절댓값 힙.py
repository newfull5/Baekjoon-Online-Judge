import heapq
import sys

input = sys.stdin.readline
heap = []

n = int(input())

for _ in range(n):
    k = int(input())
    if k == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[-1])
    else:
        heapq.heappush(heap, ((k)**2, k))
