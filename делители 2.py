n = int(input())
n_count = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            n_count += 1
    n_string = str(i)+"+"*n_count
    print(n_string)
    n_count = 0
