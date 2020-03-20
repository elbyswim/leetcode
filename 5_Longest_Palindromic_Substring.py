def isPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def longestPalindrome(s: str) -> str:
    slen = len(s)
    long = ""
    length = slen
    while long == "":
        for start in range(slen - length + 1):
            sub = s[start:start + length]
            if isPalindrome(sub):
                long = sub
                break
        length -= 1
    return long

print(longestPalindrome("abab"*250))