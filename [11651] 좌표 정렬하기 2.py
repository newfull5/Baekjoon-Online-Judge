t = int(input())
arr = []

for _ in range(t):
    arr.append(list(map(int, input().split())))

arr = sorted(arr, key = lambda x:x[0])

arr = sorted(arr, key = lambda x:x[-1])

for a,b in arr:
    print(str(a)+' '+str(b))
