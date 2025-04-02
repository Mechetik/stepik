n = int(input())
list_sum = []
list_kon = []
for i in range(n):
    list_sum.append(int(input()))
for i in range(0, n, 2):
    x_prom = list_sum[i]
    list_kon.append(x_prom)
print(list_kon)
