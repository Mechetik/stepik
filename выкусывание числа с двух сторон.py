n = int(input())
n_abs = abs(n)
quantity_digits = 1
while n_abs // 10 != 0:   #нахождение количества разрядов числа
    quantity_digits += 1
    n_abs = n_abs // 10
print(quantity_digits)
print(n)
quant= quantity_digits//2
for _ in range(quant):
    n = n - (abs(n) // (10**(quantity_digits - 1))) * 10**(quantity_digits - 1)  #выкусывание первой цифры
    n = n // 10  #выкусывание последней цифры
    quantity_digits -= 2
    print(n)