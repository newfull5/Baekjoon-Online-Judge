n = int(input())

arr = list(map(int, input().split()))

manum = max(arr)

print(sum(map(lambda x: x/manum * 100, arr))/n)
