import fractions

input()
arr = list(map(int, input().split()))

for i in range(1,len(arr)):
    temp = fractions.Fraction(arr[0],arr[i])
    print(f'{temp.numerator}/{temp.denominator}')
