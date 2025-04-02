s = input()
if len(s) % 2 == 0:
    x1 = len(s) // 2
else:
    x1 = (len(s) // 2) + 1
s_new = s[x1:]+s[:x1]
print(s_new)
