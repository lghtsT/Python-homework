X = int(input())
cnt = 0

N = 0
while (N + 1) * (N + 1) <= X:
    N += 1

for i in range (1, N + 1):
    if X % i == 0:
        cnt += 1
        
print(cnt)