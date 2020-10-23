a,b,c = map(int, input().split())

answer = ((a**2) / ((b**2) + (c**2)))**(1/2)

print(int(answer * b), int(answer * c))
