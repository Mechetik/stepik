n = int(input())
quantity_digits = 1
n_abs = abs(n)
while n_abs // 10 != 0:
    quantity_digits += 1
    n_abs = n_abs // 10
for _ in range(quantity_digits-3):
    n //= 10
m = n % 10
print(m)
