def f(temp):
    n = len(temp)
    return n*(n+1)//2

for _ in range(int(input())):
    string = input()
    print(sum(map(lambda x: f(x), string.split('X'))))
