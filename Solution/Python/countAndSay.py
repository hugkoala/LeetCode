class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        r
        """
        if n == 0:
            return ''
        else:
            return self.count(n)

    def count(self, n):

        if n == 1:
            return '1'
        else:
            laststr = self.count(n - 1)
            result = ''

            idx = 0
            cnt = 0
            complexStr = laststr[0]
            while idx < len(laststr):
                if complexStr != laststr[idx]:
                    result += str(cnt) + complexStr
                    cnt = 1
                    complexStr = laststr[idx]
                else:
                    cnt += 1
                idx += 1
            else:
                result += str(cnt) + complexStr

            return result



