import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of first matrix")
a = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    a.append(row)

print("Enter elements of second matrix")
b = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    b.append(row)

result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(a[i][j] + b[i][j])
    result.append(row)

print("Addition using list:")
for row in result:
    print(row)

x = np.array(a)
y = np.array(b)
print("Addition using NumPy:")
print(x + y)
