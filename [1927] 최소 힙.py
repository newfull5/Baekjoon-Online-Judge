import heapq, sys

arr = []

n = int(sys.stdin.readline())

for _ in range(n):
    input_ = int(sys.stdin.readline())
    if input_ == 0:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr,input_)
