a,b = map(int, input().split())

parent = [i for i in range(a+1)]

def find(c):
    if parent[c] != c:
        parent[c] =  find(parent[c])
        return parent[c]
    return c

def union(a,b):
    a,b = find(a), find(b)
    a,b = max(a,b), min(a,b)
    if a != b:
        parent[a] = b

for _ in range(b):
    a,b,c = map(int, input().split())
    
    if a == 0:
        union(b,c)
    else:
        if find(b) == find(c):
            print('YES')
        else:
            print('NO')
