n = int(input())
n_summ, n_mnozh, m = 0, 1, 1
for j in range(1, n+1):
    m = j
    for i in range(1, m+1):
        n_mnozh *= i
    n_summ += n_mnozh
    n_mnozh = 1
print(n_summ)
