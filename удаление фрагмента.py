s = input()
start_s = s.find("h")
finish_s = s.rfind("h")
s_cut = s[start_s:finish_s+1]
print(s.replace(s_cut, ""))
