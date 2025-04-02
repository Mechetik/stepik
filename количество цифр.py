s = input()
s1 = '0123456789'
sum = 0
for i in range(len(s)):
    if s[i] in s1:
        sum += 1
print(sum)
