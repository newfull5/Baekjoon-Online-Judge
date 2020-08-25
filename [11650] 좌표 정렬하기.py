arr = []
for _ in range(int(input())):
    a,b = map(int, input().split())
    arr.append([a,b])

arr = sorted(arr, key=lambda x: x[1])
arr = sorted(arr, key=lambda x: x[0])

for a,b in arr:
    print('{} {}'.format(a,b))
