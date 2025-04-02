a= int(input())
if a>=8:
    if a%2==0:
        print("31")
    else:
        print("30")
elif a%2>0:
    print("31")
elif a==2:
    print("28")
else:    
    print("30")