n = int(input())
n_ost = 0
n_string = ""
while n != 0:
    n_ost = n % 2
    n = n//2
    n_string = str(n_ost)+n_string
print(n_string)
