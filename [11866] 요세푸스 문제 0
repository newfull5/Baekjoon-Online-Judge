a,b = map(int, input().split())
b -= 1

lists = list(range(1,1+a))

index = 0

answer = '<'

while lists:
    index = (index + b) % len(lists)
    answer += str(lists.pop(index)) + ', '

print(answer[:-2] + '>')
