def groupAnagrams(strs):
    seen = {}
    for string in strs:
        key = str(sorted(list(string)))
        # if key in seen:
        #     seen[key].append(string)
        # else:
        #     seen[key] = [string]
        seen[key] = seen.get(key, list()).append(string)
    return [value for value in seen.values()]


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
