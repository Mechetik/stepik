n = int(input())
n_summ, n_mnozh = 0, 1
for i in range(1, n+1):
    n_mnozh *= i
    n_summ += n_mnozh
print(n_summ)
