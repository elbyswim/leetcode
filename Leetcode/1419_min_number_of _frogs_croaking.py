def minNumberOfFrogs(croakOfFrogs):
    if len(croakOfFrogs) % 5 != 0:
        return -1
    if len(croakOfFrogs) == 0:
        return 1
    if croakOfFrogs[0] != 'c':
        return -1
    frogs = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
    for letter in croakOfFrogs:
        if letter == 'c':
            if frogs['k'] > 0:
                frogs['k'] -= 1
            frogs['c'] += 1
        elif letter == 'r':
            if frogs['c'] > 0:
                frogs['r'] += 1
                frogs['c'] -= 1
            else:
                return -1
        elif letter == 'o':
            if frogs['r'] > 0:
                frogs['o'] += 1
                frogs['r'] -= 1
            else:
                return -1
        elif letter == 'a':
            if frogs['o'] > 0:
                frogs['a'] += 1
                frogs['o'] -= 1
            else:
                return -1
        elif letter == 'k':
            if frogs['a'] > 0:
                frogs['k'] += 1
                frogs['a'] -= 1
            else:
                return -1
    if sum(frogs[l] for l in list('croa')) > 0:
        return -1
    else:
        return frogs['k']


assert minNumberOfFrogs('croakcroak') == 1, 1
assert minNumberOfFrogs('ccroakroak') == 2, 2
assert minNumberOfFrogs('croakcrook') == -1, 3
assert minNumberOfFrogs('croakcroa') == -1, 4
