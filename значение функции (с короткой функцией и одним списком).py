n = int(input())
list_strings = []
for i in range(n):
    x = int(input())
    print(x)
    list_strings.append((x + 1)**2)
print("")
print(*list_strings, sep='\n')
