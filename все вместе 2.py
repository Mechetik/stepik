n = int(input())
first_last_digit = n % 10
count_3 = 0
count_last_digit = 0
count_even = 0
sum_five = 0
multiply_7 = 1
count_05 = 0
while n != 0:
    last_digit = n % 10
    if last_digit == 3:  # проверка на тройки
        count_3 += 1
    if last_digit == first_last_digit:  # проверка на последнюю цифру
        count_last_digit += 1
    if last_digit % 2 == 0:  # проверка на четность
        count_even += 1
    if last_digit > 5:  # проверка на пятерки
        sum_five += last_digit
    if last_digit > 7:  # проверка на семерки
        multiply_7 *= last_digit
    if last_digit == 0 or last_digit == 5:  # проверка на нули и пятерки
        count_05 += 1
    n //= 10
print(count_3)
print(count_last_digit)
print(count_even)
print(sum_five)
print(multiply_7)
print(count_05)
