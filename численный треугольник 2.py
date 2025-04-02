n = int(input())
m = 0
sum = 1
for i in range(n + 1):
    m += 1
    for j in range(1, m):
        print(sum, end="")
        sum += 1
    print()
