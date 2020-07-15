for k in range(int(input())):
    
    left = [1,0]
    right = [0,1]
    n = int(input())
    if n == 0:
        print('1 0')
        continue
    if n == 1:
        print('0 1')
        continue
    
    for _ in range(n-1):
        left,right = right, [left[0] + right[0], left[1]+right[1]]
    
    print('{} {}'.format(right[0],right[1]))
