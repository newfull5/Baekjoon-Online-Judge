'''
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
'''
#2020.06.23
N = int(input())
k = int(input())
s = [[0]*(N+1) for _ in range(N+1)]

for _ in range(k):
    a,b = map(int, input().split())
    s[a][b] = 1
    s[b][a] = 1


def bfs(start):
    visit = [start]
    queue = [start]
    
    while queue:
        temp = queue.pop(0)
        for i in range(N+1):
            if s[temp][i] == 1 and (i not in visit):
                queue.append(i)
                visit.append(i)
                
    return visit

print(len(bfs(1))-1)
