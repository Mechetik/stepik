s = input()
sum_plus = 0
s_previous = s[0]
for i in range(1, len(s)):
    if s[i] == s_previous:
        sum_plus += 1
    s_previous = s[i]
print(sum_plus)
