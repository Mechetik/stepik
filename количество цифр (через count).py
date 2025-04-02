s = input()
sum = 0
for i in range(10):
    s_num = s.count(str(i))
    if (0 <= s_num <= 9):
        sum += s_num
print(sum)
