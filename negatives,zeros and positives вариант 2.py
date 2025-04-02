n = int(input())
negatives = []
zeros = []
positives = []
for _ in range(n):
    n_numbers = int(input())
    if n_numbers < 0:
        negatives.append(n_numbers)
    if n_numbers == 0:
        zeros.append(n_numbers)
    if n_numbers > 0:
        positives.append(n_numbers)
print(*negatives, sep="\n")
print(*zeros, sep="\n")
print(*positives, sep="\n")
