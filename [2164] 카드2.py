n = int(input())

if n == 1:
    print(1)
    
if n == 2:
    print(2)
    
for k in range(1,20):
    if 2**k < n <= 2**(k+1):
        print(2 * ([i for i in range((2**k)+1, (2**(k+1))+1)].index(n)+1))
        break
