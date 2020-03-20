def longestSubstringWithoutDuplication(string):
    if len(string) <= 1:
        return string
    seen = {string[0]:0}
    maxstart = 0
    maxend = 0
    start = 0
    i = 1
    while i < len(string):
        if string[i] in seen:
            if start <= seen[string[i]]:
                start = seen[string[i]] + 1
        elif i - start > maxend - maxstart:
            maxend, maxstart = i, start
        seen[string[i]] = i
        i += 1
    return string[maxstart:maxend + 1]

longestSubstringWithoutDuplication('abccdeaabbcddef')