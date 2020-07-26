n = int(input())

for _ in range(n):
    a,b = input().split()
    
    print(''.join(list(map(lambda x: int(a)*x, list(b)))))
