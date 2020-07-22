answer = []
for _ in range(10):
    answer.append(int(input()) % 42)
        
print(len(set(answer)))
