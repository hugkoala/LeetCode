class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """


    def checkPalindrome(self, s, i, j, idx):
        if idx > len(s) or idx < 0:
            return ''
        elif s[i] == s[j]:
            if i + 1 < len(s) and j - 1 > 0:
                return checkPalindrome(s, i + 1, j - 1, idx)
            else:
                return s[j : i + 1]
        else:
            str1 = checkPalindrome(s, i + 1, j + 1, idx + 1)