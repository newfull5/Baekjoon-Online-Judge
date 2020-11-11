input()
temp = input().split()
Y = sum(map(lambda x: ((int(x)//30) + 1)*10, temp))

M = sum(map(lambda x: ((int(x)//60) + 1)*15, temp))

if Y < M:
    print('Y', Y)
elif M < Y:
    print('M', M)
else:
    print('Y','M',Y)
