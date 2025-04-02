s = input()
f = ''
strings = s.split()
for i in range(len(strings)):
    f += strings[i][0] + '.'
print(f)
