n = int(input())
strings = []
search_strings = []
flag = 0
for _ in range(n):
    strings.append(input())
k = int(input())
for _ in range(k):
    search_strings.append(input())
for i in range(n):
    for j in range(k):
        if search_strings[j].lower() not in strings[i].lower():
            flag = 1
    if flag == 0:
        print(strings[i])
    else:
        flag = 0
