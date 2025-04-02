n = int(input()) 
n_1 = 1
n_2 = 0
print(n_1, end = ' ')
for _ in range(2,n+1):
    Sum = n_1 + n_2
    print(Sum, end = ' ')  
    n_2 = n_1
    n_1 = Sum
    
     