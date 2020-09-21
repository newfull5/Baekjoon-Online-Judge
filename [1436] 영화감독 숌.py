n = int(input())
cnt = 0
answer = 666

while True:
    if '666' in str(answer):
        cnt += 1
    if cnt == n:
        print(answer)
        break
    answer += 1
    
