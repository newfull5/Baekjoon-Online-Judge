import sys

input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(int(input())):
    arr.append(tuple(map(int, input().split())))

arr = sorted(arr, key = lambda x: x[-1])

visited = [arr[0][0]]
answer = 0

while len(visited) != n:
    
    for a,b,c in arr:
        if a in visited and b in visited:
            continue
            
        if a in visited or b in visited:
            visited += [a,b]
            visited = list(set(visited))
            answer += c
            break
            
print(answer)
