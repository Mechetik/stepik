n = int(input())
m = 0
n_max, n_min = 0, 10
while n != 0:
    m = n % 10  # последняя цифра числа
    if n_max < m:
        n_max = m    
    if n_min > m:
        n_min = m
    n = n // 10  #выкусывание последней цифры
print ("Максимальная цифра равна", n_max)
print ("Минимальная цифра равна", n_min)