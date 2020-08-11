t = int(input())

for _ in range(t):

    n = int(input())

    length = [1, 1, 1, 2, 2]

    if n <= 5:
        print(length[n-1])
    else:
        i = 0

        while len(length) != n:
            length.append(length[i]+length[-1])
            i += 1
        print(length[-1])
