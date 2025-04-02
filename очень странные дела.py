n = int(input())
odi_sum = 0
for _ in range(n):
    s = input()
    m = s.count('11')
    if m > 2:
        odi_sum += 1
print(odi_sum)
