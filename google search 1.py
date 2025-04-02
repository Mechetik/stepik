n = int(input())
strings = []
for _ in range(n):
    strings.append(input())
f = input()
for i in range(n):
    if f.lower() in strings[i].lower():
        print(strings[i])
