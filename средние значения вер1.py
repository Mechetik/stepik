from math import sqrt
a = float(input())
b = float(input())
s_arifm = (a+b)/2
s_geom = sqrt(a*b)
s_garm = (2*a*b)/(a+b)
s_qvad = sqrt((a**2+b**2)/2)
print(s_arifm,s_geom,s_garm,s_qvad, sep = "\n")