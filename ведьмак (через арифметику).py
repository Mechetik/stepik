n = int(input())
a = n // 25
b = (n - a * 25) // 10
c = ((n - (a * 25 + b * 10))) // 5
d = n - (a*25+b*10+c*5)
print(a+b+c+d)

#while n - 25 >= 25:
#    quantity_five += 1
#    n -= 25
#while n - 10 >= 10:
#    quantity_five += 1
#    n -= 10
#while n - 5 >= 5:
#    quantity_five += 1
#    n -= 5
#while n - 1 >= 1:
#    quantity_five += 1
#    n -= 1
#print(quantity_five)
