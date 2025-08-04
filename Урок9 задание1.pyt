N = int(input())

numbers = list(map(int, input().split()))

assert len(numbers) == N

diff = set(numbers)

print(len(diff))