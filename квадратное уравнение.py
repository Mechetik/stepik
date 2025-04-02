from math import sqrt
a = float(input())
b = float(input())
c = float(input())
D = (b**2) - (4*a*c)
if D == 0:
    print((-1*b)/(2*a))
elif D>0:
    x1 = ((-1*b)-sqrt(D))/(2*a)
    x2 = ((-1*b)+sqrt(D))/(2*a)
    if x2>x1:
        print(x1,x2, sep = '\n')
    else:
        print(x2,x1, sep = '\n')
else:
    print("Нет корней")