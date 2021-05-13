def longestCommonSubsequence(str1, str2):
    # Write your code here.
    if len(str1) == 0 or len(str2) == 0:
        return []
    memo = [[[] for _ in range(len(str2))] for _ in range(len(str1))]
    for i in range(len(str1)):
        for j in range(len(str2)):
            if i == j == 0:
                if str1[i] == str2[j]:
                    memo[i][j].append(str1[i])
            elif i == 0:
                if str1[i] == str2[j]:
                    memo[i][j].append(str1[i])
                else:
                    memo[i][j] = memo[i][j - 1]
            elif j == 0:
                if str1[i] == str2[j]:
                    memo[i][j].append(str1[i])
                else:
                    memo[i][j] = memo[i - 1][j]
            if i != 0 and j != 0:
                if str1[i] == str2[j]:
                    memo[i][j] = memo[i - 1][j - 1] + [str1[i]]
                elif len(memo[i - 1][j]) <= len(memo[i][j - 1]):
                    memo[i][j] = memo[i][j - 1]
                else:
                    memo[i][j] = memo[i - 1][j]
    return memo[len(str1) - 1][len(str2) - 1]


print(longestCommonSubsequence('apples', 'abcde'))
