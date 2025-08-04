numbers = list(map(int, input().split()))
been = set()

for num in numbers:
    if num in been:
        print("YES")
    else:
        print("NO")
        been.add(num)