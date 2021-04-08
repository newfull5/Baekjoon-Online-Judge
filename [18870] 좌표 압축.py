input()
arr = list(map(int, input().split()))

diction = {}
for i,v in enumerate(sorted(list(set(arr)))):
    diction[v]=i

print(*[diction[a] for a in arr])
