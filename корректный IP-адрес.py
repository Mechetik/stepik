ip_flag = True
strings = input().split('.')
for i in range(len(strings)):
    n = int(strings[i])
    if not (0 <= n <= 255):
        ip_flag = False
if ip_flag == True:
    print('ДА')
else:
    print('НЕТ')
