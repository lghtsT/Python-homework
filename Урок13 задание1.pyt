import random

rows, cols = 10, 10

matrix1 = []
for _ in range(rows):
    row = []
    for _ in range(cols):
        row.append(random.randint(-200, 200))
    matrix1.append(row)

matrix2 = []
for _ in range(rows):
    row = []
    for _ in range(cols):
        row.append(random.randint(-100, 100))
    matrix2.append(row)

print("Первая матрица:")
for row in matrix1:
    print(row)

print("Вторая матрица:")
for row in matrix2:
    print(row)

matrix_sum = []
for i in range(rows):
    row_sum = []
    for j in range(cols):
        row_sum.append(matrix1[i][j] + matrix2[i][j])
    matrix_sum.append(row_sum)

print("Сумма двух матриц:")
for row in matrix_sum:
    print(row)