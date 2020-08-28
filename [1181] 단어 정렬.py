t = int(input())
arr = []

for _ in range(t):
    arr.append(input())

arr = list(set(arr))
arr = sorted(arr)
arr = sorted(arr, key=lambda x: len(x))

for char in arr:
    print(char)
