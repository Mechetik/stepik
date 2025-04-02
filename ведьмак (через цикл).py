n = int(input())
quantity_coin = 0
while n >= 25:
    quantity_coin += 1
    n = n - 25
while n >= 10:
    quantity_coin += 1
    n = n-10
while n >= 5:
    quantity_coin += 1
    n = n - 5
while n >= 1:
    quantity_coin += 1
    n = n - 1
print(quantity_coin)
