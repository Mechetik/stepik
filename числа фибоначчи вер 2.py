n = int(input()) 
n_1, n_2 = 1,0
for _ in range(n):
    print(n_1, end = ' ') 
    n_2, n_1 = n_1, n_1 +n_2
       