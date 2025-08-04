def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Введите натуральное число: "))

fact_num = factorial(num)

factorials_list = [factorial(i) for i in range(num, 0, -1)]

print(f"Факториал числа {num} равен: {fact_num}")
print("Список факториалов от этого числа до 1:", factorials_list)