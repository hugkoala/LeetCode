class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''
        elif len(s) == 1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        else:
            longestPalindrome = ''

            for idx in range(0, len(s)):
                if idx + 1 < len(s):
                    isPalindrome = None
                    i = idx + 1
                    j = idx
                    while isPalindrome or isPalindrome == None:
                        if s[i] == s[j]:
                            if i + 1 >= len(s) or j - 1 < 0:
                                isPalindrome = False
                                if len(longestPalindrome) < i - j + 1:
                                    longestPalindrome = s[j: i + 1]
                            else:
                                isPalindrome = True
                                i += 1
                                j -= 1
                        else:
                            if isPalindrome:
                                if len(longestPalindrome) < i - j - 1:
                                    longestPalindrome = s[j + 1: i]
                            isPalindrome = False
                if idx + 1 < len(s) and idx - 1 >= 0:
                    isPalindrome = None
                    i = idx + 1
                    j = idx - 1
                    while isPalindrome or isPalindrome == None:
                        if s[i] == s[j]:
                            if i + 1 >= len(s) or j - 1 < 0:
                                isPalindrome = False
                                if len(longestPalindrome) < i - j + 1:
                                    longestPalindrome = s[j: i + 1]
                            else:
                                isPalindrome = True
                                i += 1
                                j -= 1
                        else:
                            if isPalindrome:
                                if len(longestPalindrome) < i - j - 1:
                                    longestPalindrome = s[j + 1: i]
                            isPalindrome = False
            if longestPalindrome == '':
                return s[0]
            else:
                return longestPalindrome
