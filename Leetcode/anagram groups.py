def groupAnagrams(words):
    seen = {}
    for word in words:
        sorted = list(word)
        sorted.sort()
        key = ''.join(sorted)
        if key in seen:
            seen[key].append(word)
        else:
            seen[key] = [word]
    anagrams = []
    for group in seen:
        anagrams.append(group)
    return anagrams
