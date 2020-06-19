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
