a = input()
if sum(map(int, list(a))) % 3 == 0 and '0' in list(a):
    print(''.join(sorted(a, reverse = True)))
else:
    print(-1)
