N = int(input())

s = []

for _ in range(N):
    s.append(list(map(int, list(str(input())))))

for i in range(len(s)):
    s[i] = list(map(int, s[i]))

def bfs(x,y,cnt):
    visit = [[x,y]]
    queue = [[x,y]]
    
    while queue:
        x,y = queue.pop(0)
        s[x][y] = cnt
        visit.append([x,y])
        
        if x != 0 and s[x-1][y] == 1 and ([x-1, y] not in visit):
            queue.append([x-1, y])
            
        if y != 0 and s[x][y-1] == 1 and ([x, y-1] not in visit):
            queue.append([x, y-1])
            
        if x != N-1 and s[x+1][y] == 1 and ([x+1, y] not in visit):
            queue.append([x+1, y])
            
        if y != N-1 and s[x][y+1] == 1 and ([x, y+1] not in visit):
            queue.append([x, y+1])

cnt = 1
for i in range(N):
    for j in range(N):
        if s[i][j] == 1:
            cnt += 1
            bfs(i,j,cnt)

s = sum(s,[]) 

print(cnt-1)

for i in range(2,cnt+1):
    print(s.count(i))
