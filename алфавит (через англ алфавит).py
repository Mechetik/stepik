words = []
alphavit = "abcdefghijklmnopqrstuvwxyz"
words.extend(alphavit)
for i in range(26):
    words[i] = words[i]*(i+1)
print(words)
