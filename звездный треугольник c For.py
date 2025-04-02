n = int(input())
n_flag  = 0
for i in range(1,n+1):
    if i > (int(n / 2)+1):
        n_flag -= 2
    nn = i + n_flag
    print("*" * nn)

