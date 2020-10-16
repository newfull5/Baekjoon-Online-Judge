import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

s = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    s[a][b] = 1
    s[b][a] = 1

def DFS(start, visited):
    visited += [start]
    
    for i in range(n+1):
        if s[start][i] == 1 and (i not in visited):
            DFS(i, visited)
    return visited
    
print(len(DFS(1,[]))-1)
