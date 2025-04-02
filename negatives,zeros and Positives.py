n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
for i in range(n):
    if numbers[i] < 0:
        print(numbers[i])
for i in range(n):
    if numbers[i] == 0:
        print(numbers[i])
for i in range(n):
    if numbers[i] > 0:
        print(numbers[i])
