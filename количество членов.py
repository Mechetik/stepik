input_text = input()
num_text = 0
while input_text != 'стоп' and input_text != 'хватит' and input_text != 'достаточно':
    num_text += 1
    input_text = input()
print(num_text)