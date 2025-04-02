n = int(input())
strings = []
strings.append(input())
for i in range(n - 1):
    s = input()
    if s not in strings:
        strings.append(s)
print(*strings, sep='\n')
