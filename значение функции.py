n = int(input())
list_strings = []
list_strings_1 = []
for i in range(n):
    x = int(input())
    list_strings.append(x)
    list_strings_1.append(x**2 + 2 * x + 1)
print(*list_strings, sep='\n')
print("")
print(*list_strings_1, sep='\n')
