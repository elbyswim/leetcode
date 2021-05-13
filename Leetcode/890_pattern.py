def findAndReplacePattern(words, pattern):
    n = len(pattern)
    matches = []
    for word in words:
        dict = {}
        same_pattern = True
        for i in range(n):
            if pattern[i] in dict:
                if word[i] != dict[pattern[i]]:
                    same_pattern = False
            else:
                dict[pattern[i]] = word[i]
        if same_pattern:
            matches.append(word)
    return matches


print(findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))
