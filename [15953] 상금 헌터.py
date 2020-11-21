def reward_2017(num):
    if num == 0:
        return 0
    if num == 1:
        return 5000000
    if num <= 3:
        return 3000000
    if num <= 6:
        return 2000000
    if num <= 10:
        return 500000
    if num <= 15:
        return 300000
    if num <= 21:
        return 100000
    if num > 21:
        return 0

def reward_2018(num):
    if num == 0:
        return 0
    if num == 1:
        return 5120000
    if num <= 3:
        return 2560000
    if num <= 7:
        return 1280000
    if num <= 15:
        return 640000
    if num <= 31:
        return 320000
    if num > 31:
        return 0

n = int(input())
for _ in range(n):
    a,b = map(int, input().split())
    print(reward_2017(a) + reward_2018(b))
