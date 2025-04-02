a= int(input())
b= int(input())
c = int(input())
if a>b and a>c and b>c:
    Xmax=a
    Xmin=c
    else:
    Xmax    
    print (b)
elif a>b and a>c and c>b:
    print (c)
elif b>a and b>c and a>c:
    print (a)    
elif b>a and b>c and c>a:
    print (c)
elif c>a and c>b and a>b:
    print (a)
else:
    print(b)