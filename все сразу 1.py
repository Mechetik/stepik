numbers = [
    2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11,
    10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1,
    2, 14, 16, 6, 7, 5
]
numbers_7, numbers_17 = 0, 0
for i in range(len(numbers)):
    if numbers[i] == 7:
        numbers_7 = 1
    if numbers[i] == 17:
        numbers_17 = 1
print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
if (numbers_7+numbers_17) == 2:
    print("YES")
else:
    print("NO")
del numbers[0]
del numbers[-1]
print(numbers)
