N = int(input())
numbers = []

for _ in range(N):
    num = int(input())
    if abs(num) > 10**5:
        print("превышает 10e5 по модулю")
        pass
    numbers.append(num)

numbers.reverse()

print(' '.join(map(str, numbers)))