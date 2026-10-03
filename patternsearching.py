txt = input()
pat = input()

m = len(pat)
lps = [0] * m

length = 0
i = 1

while i < m:
    if pat[i] == pat[length]:
        length += 1
        lps[i] = length
        i += 1
    elif length:
        length = lps[length - 1]
    else:
        i += 1

i = 0
j = 0

while i < len(txt):
    if txt[i] == pat[j]:
        i += 1
        j += 1

        if j == m:
            print(i - j)
            j = lps[j - 1]
    elif j:
        j = lps[j - 1]
    else:
        i += 1
