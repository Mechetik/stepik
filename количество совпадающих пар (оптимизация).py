strings = input().split()
pairs = 0
for i in range(len(strings)):
    for j in range(i+1, len(strings)):
        if strings[j] == strings[i]:
            pairs += 1
print(pairs)
