strings = input().split()
pairs = 0
for i in range(len(strings)):
    strings[i] = int(strings[i])
for i in range(1, len(strings)):
    first_pos = strings[i-1]
    for j in range(i, len(strings)):
        if strings[j] == first_pos:
            pairs += 1
print(pairs)
