mon = [0,31,28,31,30,31,30,31,31,30,31,30,31]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

a, b = map(int, input().split())

sum_ = 0

for i in range(a):
    sum_ += mon[i]
    
sum_ += b

print(day[sum_%7])
