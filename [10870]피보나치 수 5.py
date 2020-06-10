def fib(K):
    if K == 1:
        return 1
    if K == 0:
        return 0
    else:
        return fib(K-1) + fib(K-2)
    
print(fib(int(input())))
