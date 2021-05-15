# 1 Arrays and Strings

# 1.1
def is_unique(s):
    seen = set()
    for c in s:
        if c in seen:
            return False
        else:
            seen.add(c)
    return True


def is_unique2(s):
    return len(s) == len(set(s))


# 1.2
# O(n) time and space
def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    c1, c2 = {}, {}
    for i in range(len(s1)):
        if s1[i] in c1:
            c1[s1[i]] += 1
        else:
            c1[s1[i]] = 0
        if s2[i] in c2:
            c2[s2[i]] += 1
        else:
            c2[s2[i]] = 0
    for key in c1:
        if c1[key] != c2[key]:
            return False
    return True


# O(n log n) time
def check_permutation2(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(list(s1)) == sorted(list(s2))


# 1.3
def urlify(s):
    s = s.strip()
    flag = False
    answer = []
    for c in s:
        if c == ' ' and flag:
            continue
        elif c == ' ':
            flag = True
            answer.append('%20')
        else:
            flag = False
            answer.append(c)
    return ''.join(answer)


# 1.4
def palindrome_permutation(s):
    seen = {}
    odd = 0
    for c in s:
        if c.isalpha():
            if c in s:
                seen[c] += 1
            else:
                seen[c] = 1
                odd += 1 if seen[c] % 2 else - 1
    return odd <= 1


def palindrome_permutation1(s):
    from collections import Counter
    seen = Counter(s)
    odd = 0
    for c in seen:
        if seen[c] % 2:
            odd += 1
    return odd <= 1


# 1.5
def one_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    i = 0
    while i < min(len(s1), len(s2)) and s1[i] == s2[i]:
        i += 1
    if i == min(len(s1), len(s2)):
        return True
    j = -1
    while j <= 0 and s1[j] == s2[j]:
        j -= 1
    j += max(len(s1), len(s2))
    return i == j


# 1.6
def string_compression(s):
    i = 0
    ans = []
    while i < len(s):
        ans.append(s[i])
        count = 1
        i += 1
        while i < len(s) and s[i] == ans[-1]:
            i += 1
            count += 1
        ans.append(str(count))
    ans = ''.join(ans)
    return ans if len(ans) < len(s) else s


# 1.7
def rotate(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(n // 2 + 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp
    return matrix


# 1.8
def zero_matrix(matrix):
    rows = set()
    cols = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in rows or j in cols:
                matrix[i][j] = 0
    return matrix


# 1.9
def isSubstring(s1, s2):
    return s2 in s1


def string_rotation(s1, s2):
    return isSubstring(s1 + s1, s2)
