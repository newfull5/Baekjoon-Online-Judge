N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, str(input()))))
i,j = 0,0
distance = [[0]*M for _ in range(N)]
queue = [[i,j]]
visit = []
distance[0][0] = 1

while queue:
    
    [i,j] = queue.pop(0)
    visit.append([i,j])
    
    if i > 0 and maze[i-1][j] == 1 and [i-1, j] not in visit and [i-1, j] not in queue:
        queue.append([i-1,j])
        distance[i-1][j] = distance[i][j] + 1
        
    if j > 0 and maze[i][j-1] == 1 and [i, j-1] not in visit and [i, j-1] not in queue:
        queue.append([i,j-1])
        distance[i][j-1] = distance[i][j] + 1
        
    if i < N-1 and maze[i+1][j] == 1 and [i+1, j] not in visit and [i+1, j] not in queue:
        queue.append([i+1,j])
        distance[i+1][j] = distance[i][j] + 1
        
    if j < M-1 and maze[i][j+1] == 1 and [i, j+1] not in visit and [i, j+1] not in queue:
        queue.append([i,j+1])
        distance[i][j+1] = distance[i][j] + 1
        
print(distance[N-1][M-1])
