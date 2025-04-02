n = int(input()) 
n_1, n_2,S = 1,0,''
for _ in range(n):
    S = S + str(n_1) + ' '
    n_2, n_1 = n_1, n_1 +n_2
print(S)    