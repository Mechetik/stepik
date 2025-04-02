n = int(input())
last_digit = 0
m = n % 10
n_similar = "YES"
while n != 0:
    last_digit = n % 10  # последняя цифра числа
    if last_digit < m:
        n_similar = "NO"
    m = last_digit
    n = n // 10  # выкусывание последней цифры
print(n_similar)
