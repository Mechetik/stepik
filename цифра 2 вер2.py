s = input()
flag_s = 0
for i in range(len(s)):
    if s[i] in "0123456789":
        print("Цифра")
        break
else:
    print("Цифр нет")
