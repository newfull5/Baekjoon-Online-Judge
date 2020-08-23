arr = []

length = int(input())

for _ in range(length):
    arr.append(list(map(int, input().split())))

for crt in arr:
    cnt = 1
    
    for nxt in arr:
        if crt[0] != nxt[0] and crt[1] != nxt[1]:
            if crt[0] <= nxt[0] and crt[1] <= nxt[1]:
                cnt += 1
    print(cnt, end=' ')
