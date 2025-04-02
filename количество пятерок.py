n = int(input())
quantity_five = 0
while not n < 1 and not n > 5:
    if n == 5:
        quantity_five +=1
    n = int(input())
print(quantity_five)
