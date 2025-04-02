n = int(input())
n_summ = 0
while n > 9:
    while n != 0:
        last_digit = n % 10
        n_summ += last_digit
        n = n // 10
    n = n_summ
    n_summ = 0
print(n)
