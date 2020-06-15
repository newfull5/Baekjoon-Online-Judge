n = int(input())
m = int(input())
s = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,input().split())
    s[x][y] = 1
    s[y][x] = 1
    
def dfs(start, visited):
    visited += [start]
    
    for i in range(n+1):
        if s[start][i] == 1 and (i not in visited):
            dfs(i, visited)
            
    return visited


print(len(dfs(1, []))-1)
