n = int(input())
n_summ = 0
while n != 0:
    while n != 0:
        last_digit = n % 10
        n_summ += last_digit
        n = n // 10
    n = n_summ
    if n // 10 == 0:
        break
    n_summ = 0
print(n_summ)
