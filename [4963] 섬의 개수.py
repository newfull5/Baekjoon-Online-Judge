import sys
sys.setrecursionlimit(4000)

def Solution(width,height,board):
    move = [(-1,0),(1,0),(0,-1),(0,1),(-1,1),(1,1),(-1,-1),(1,-1)]
    answer = 0

    def DFS(H, W):
        nonlocal board
        nonlocal answer

        for a,b in move:

            # Index Error
            if H+a < 0 or W+b < 0:
                continue
            if H+a == height or W+b == width:
                continue

            if board[H+a][W+b] == '1':
                board[H+a][W+b] = answer
                DFS(H+a, W+b)

    for h in range(height):
        for w in range(width):
            if board[h][w] == '1':
                answer += 1
                board[h][w] = answer

                DFS(h,w)
    return answer


 
while True:
    width, height = map(int, input().split())
    
    if width == 0 and height == 0:
        break
        
    board = []
    for _ in range(height):
        board.append(input().split())
        
    print(Solution(width,height,board))
