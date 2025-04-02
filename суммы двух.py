n = int(input())
list_sum = []
previous_num = int(input())
for i in range(1, n):
    current_num = int(input())
    list_sum.append(previous_num+current_num)
    previous_num = current_num
print(list_sum)
