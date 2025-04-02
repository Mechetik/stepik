s = input()
s_f = s.count("f")
if s_f == 0:
    print("-2")
elif s_f == 1:
    print("-1")
else:
    s1 = s.replace("f", "", 1)
    print(s1.find("f")+1)
