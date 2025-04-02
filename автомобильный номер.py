s = input()
s_flag = True
if len(s) == 9 or len(s) == 10:
    s_flag = True
    if s[1:4].isdigit() != True:
        s_flag = False
    if s[6] != "_":
        s_flag = False
    if s[7:].isdigit() != True:
        s_flag = False
    if s[0] not in "АВЕКМНОРСТУХ":
        s_flag = False
    if s[4] not in "АВЕКМНОРСТУХ":
        s_flag = False
    if s[5] not in "АВЕКМНОРСТУХ":
        s_flag = False
else:
    s_flag = False
if s_flag == True:
    print("YES")
else:
    print("NO")
