n = int(input())
list_sum = []
for i in range(n):
    list_sum.append(int(input()))
del list_sum[1::2]
print(list_sum)
