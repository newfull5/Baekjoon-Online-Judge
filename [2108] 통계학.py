# 평균
def mean(v) :
    return round(sum(v)/n)
 
# 중앙값
def median(v) :
    if n == 1 : return (v[0])
    else : return (v[n//2] if n%2!=0 else round((v[n//2]+v[n//2+1])/2)) # n이 홀수일땐 가운데 값 return/ 짝수일땐 가운데 두 개 평균
 
# 최빈값
from collections import Counter
def many_value(v) :
    if n == 1 : return v[0]
    c = Counter(v).most_common(2)
    return (c[1][0] if c[0][1] == c[1][1] else c[0][0])
 
# range
def min_max(v) :
    return v[n-1]-v[0]
 
n = int(input())
v = sorted([int(input()) for _ in range(n)])
 
print(mean(v))
print(median(v))
print(many_value(v))
print(min_max(v))
