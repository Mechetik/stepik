name1 = input()
name2 = input()
name3 = input()
len1 = len(name1)
len2 = len(name2)
len3 = len(name3)
l_max = max(len1,len2,len3)
l_min = min(len1,len2,len3)
l_mid = (len1+len2+len3)-(l_max+l_min)
if l_mid-l_min == l_max-l_mid:
    print('YES')
else:
    print('NO')