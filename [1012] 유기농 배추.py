"""
T = int(input())

for _ in range(T):
    a,b,c = map(int,input().split())

    s = [[0]*a for _ in range(b)]

    for k in range(c):
        a,b = map(int, input().split())
        s[b][a] = 1

    visited = []

    def dfs(cur,i):
        global visited
        global s
    
        s[cur[0]][cur[1]] = i
    
        if cur[0] != 0 and s[cur[0]-1][cur[1]] == 1:
            dfs([cur[0]-1,cur[1]],i)
        
        if cur[1] != 0 and s[cur[0]][cur[1]-1] == 1:
            dfs([cur[0],cur[1]-1],i)
        
        if cur[0] != (b-1) and s[cur[0]+1][cur[1]] == 1:
            dfs([cur[0]+1,cur[1]],i)
        
        if cur[1] != (a-1) and s[cur[0]][cur[1]+1] == 1:
            dfs([cur[0],cur[1]+1],i)

    cnt = -1
    for i in range(b):
        for j in range(a):
            if s[i][j] == 1:
                dfs([i,j], cnt)
                cnt -= 1

    print(abs(cnt+1))
"""
#2020.11.06
import sys
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline

def DFS(cnt,a,b):
    
    s[a][b] = cnt
    
    if a != (n-1):
        if s[a+1][b] == 1: #아래로 이동
            DFS(cnt, a+1, b)
    
    if a != 0:
        if s[a-1][b] == 1: #위로 이동
            DFS(cnt, a-1, b)
        
    if b != (m-1):
        if s[a][b+1] == 1: #오른쪽 이동
            DFS(cnt, a, b+1)
        
    if b != 0:
        if s[a][b-1] == 1: #왼쪽 이동
            DFS(cnt, a , b-1)

T = int(input())

for _ in range(T):
    
    m,n,k = map(int, input().split())

    s = [[0]*m for _ in range(n)]

    for _ in range(k):
        a,b = map(int, input().split())
        s[b][a] = 1

    cnt = 2
    
    for i in range(n):
        for j in range(m):

            if s[i][j] == 1:
                DFS(cnt,i,j)
                cnt += 1
                
    print(cnt-2)
