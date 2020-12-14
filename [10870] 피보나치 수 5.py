"""
def fib(K):
    if K == 1:
        return 1
    if K == 0:
        return 0
    else:
        return fib(K-1) + fib(K-2)
    
print(fib(int(input()))) 
"""

#2020.12.14
def Fib(a):
    if a == 0:
        return 0
    if a == 1:
        return 1
    return Fib(a-1) + Fib(a-2)

print(Fib(int(input())))
