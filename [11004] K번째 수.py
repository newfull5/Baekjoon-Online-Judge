import heapq

a,b = map(int, input().split())

arr = list(map(int, input().split()))
heapq.heapify(arr)

for _ in range(b-1):
    heapq.heappop(arr)
    
print(heapq.heappop(arr))
