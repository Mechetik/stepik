n = int(input())
list_prev = []
s_prom, s_kon = "", ""
for i in range(n):
    list_prev.append(input())
k = int(input())
for i in range(n):
    s_prom = list_prev[i]
    if len(s_prom) >= k:
        s_kon += s_prom[k - 1]
print(s_kon)
