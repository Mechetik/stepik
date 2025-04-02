n = int(input())
numbers = []
numbers_1 = []
for i in range(n):
    numbers.append(int(input()))
list_max = max(numbers)
list_min = min(numbers)
for i in range(len(numbers)):
    if not numbers[i] == list_max and not numbers[i] == list_min:
        numbers_1.append(numbers[i])
print(*numbers_1, sep='\n')
