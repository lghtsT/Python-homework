N = int(input())

M = list(map(int, input().split()))

assert len(M) == N

result = [M[-1]] + M[:-1]

print(' '.join(map(str, result)))