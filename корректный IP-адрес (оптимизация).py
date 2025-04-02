s = input()
for i in range(len(strings)):
    if not (0 <= int(strings[i]) <= 255):
        ip_flag = False
if ip_flag:
    print('ДА')
else:
    print('НЕТ')
