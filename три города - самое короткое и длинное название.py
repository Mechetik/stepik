name1 = input()
name2 = input()
name3 = input()
len1 = len(name1)
len2 = len(name2)
len3 = len(name3)
if len1<len2 and len1<len3:
    name_min = name1
elif len2<len1 and len2<len3:
    name_min = name2
else: 
    name_min = name3    
if len1>len2 and len1>len3:
    name_max = name1
elif len2>len1 and len2>len3:
    name_max = name2
else: 
    name_max = name3    
print(name_min)
print(name_max)