n = int(input())
s = input()
for i in range(len(s)):
    n_ord = ord(s[i]) - n
    if n_ord < 97:
        n_ord += 26
    print(chr(n_ord), end="")
