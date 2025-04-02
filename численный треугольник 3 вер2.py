n = int(input())
for i in range(n + 1):
    for j in range(1, i+1):
        print(j, end="")
    for z in range(i-1, 0, -1):
        print(z, end="")
    print()
