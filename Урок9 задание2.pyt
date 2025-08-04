list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

set1 = set(list1)
set2 = set(list2)

numbers = set1.intersection(set2)

print(len(numbers))