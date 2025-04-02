n = int(input())
n_sum, n_digits, n_average, n_first_digit, n_multi = 0, 0, 0, 0, 1
m = 0
n_last = n % 10
while n != 0:
    m = n % 10  # последняя цифра числа
    n_sum += m
    n_digits += 1
    n_multi *= m
    n = n // 10  #выкусывание последней цифры
print (n_sum)
print(n_digits)
print(n_multi)
print(n_sum / n_digits)
print(m)
print(m+n_last)