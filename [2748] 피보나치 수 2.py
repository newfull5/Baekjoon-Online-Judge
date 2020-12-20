a = 0
b = 1

for _ in range(int(input())-1):
    a,b = b, a+b
print(b)
