a,b,c = map(int, input().split())

if a+b+c < 100:
    if a<b and a<c:
        print('Soongsil')
    if b<a and b<c:
        print('Korea')
    if c<a and c<b:
        print('Hanyang')
else:
    print('OK')
