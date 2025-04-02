s = input()
flag_s = 0
for i in range(len(s)):
    if s[i] in "0123456789":
        flag_s =1
if flag_s ==1:        
    print("Цифра")
else:
    print("Цифр нет")
