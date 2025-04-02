total = 0
for calf in range(201):
    for cow in range(21):
        for bull in range(11):
            if 10 * bull + 5 * cow + 0.5 * calf == 100:
                total += 1
                if bull + cow + calf == 100:
                    print('бык =', bull, 'корова =', cow, "теленок =", calf)
print('Общее количество натуральных решений =', total)
