import sys

input = sys.stdin.readline

for _ in range(3):
    sum_ = 0
    
    for __ in range(int(input())):
        sum_ += int(input())
        
    if sum_ == 0:
        print(0)
        
    elif sum_ > 0:
        print('+')
        
    elif sum_ < 0:
        print('-')
