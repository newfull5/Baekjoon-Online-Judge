'''n,m,v = map(int, input().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
visit = [0 for i in range(n + 1)]

for i in range(m):
    x,y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1
    
    
def bfs(start):
    visited = [start]
    queue = [start]
    while queue:
        n = queue.pop(0)
        for c in range(len(matrix[start])):
            if matrix[n][c] == 1 and (c not in visited):
                visited.append(c)
                queue.append(c)
    return visited

def dfs(start, visited):
    visited += [start]
    for c in range(len(matrix[start])):
        if matrix[start][c] == 1 and (c not in visited):
            dfs(c, visited)
    return visited


print(*dfs(v,[]))
print(*bfs(v))
'''
N, M, V = map(int, input().split())
s = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    x,y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1
    
def bfs(current):
    visit = [current]
    queue = [current]
    
    while queue:
        n = queue.pop(0)
        for i in range(N+1):
            if s[n][i] == 1 and (i not in visit):
                visit.append(i)
                queue.append(i)
    return visit

def dfs(current,visit):
    visit.append(current)
    
    for i in range(N+1):
        if s[current][i] == 1 and (i not in visit):
            dfs(i, visit)
    
    return visit

print(*dfs(V,[]))
print(*bfs(V))
