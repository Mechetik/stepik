a = int(input())
b = int(input())
max_number, sum_max_number_old, sum_max_number_new = 0, 0, 0
for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            sum_max_number_new += j
    if sum_max_number_new >= sum_max_number_old:
        max_number = i
        sum_max_number_old = sum_max_number_new
    sum_max_number_new = 0
print(max_number, sum_max_number_old)
