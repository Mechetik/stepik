n = int(input())
n_step = 0
m = n // 2 + 1
for i in range(1, n + 1):
    for j in range(i):
        if i > m:
            break
        print("*", end="")
    for j in range(n - i+1):
        if i <= m:
            break
        print("*", end="")
    print()
