A = int(input())
B = int(input())
cht = []

for num in range(A, B + 1):
    if num % 2 == 0:
        cht.append(str(num))

print(' '.join(cht))