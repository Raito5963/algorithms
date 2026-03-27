# This is Knuth-Morris-Pratto (KMP)

def kmp_search(search, word):
    if not word: return 0
    t = [0] * len(word)
    j = 0
    for i in range(1, len(word)):
        while j > 0 and word[i] != word[j]:
            j = t[j-1]
        if word[i] == word[j]:
            j += 1
            t[i] = j

    m = 0 # Currently chekking start position in search
    i = 0 # Current position in word
    while m + i < len(search):
        if word[i] == search[m+i]:
            i += 1
            if i == len(word):
                return m # find
        else:
            if i > 0:
                m = m + i - t[i-1] # jamp using table
                i = t[i-1]
            else:
                m = m + 1 # if not maching, do next
                i = 0
    return -1 # not found