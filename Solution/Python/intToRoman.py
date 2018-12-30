class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 1 or num > 3999:
            return ''
        else:
            result = ''

            thousand = num // 1000
            if thousand > 0:
                result = result + self.switch(thousand, 'M', '', '')
            num = num - thousand * 1000

            hundred = num // 100
            if hundred > 0:
                result = result + self.switch(hundred, 'C', 'D', 'M')
            num = num - hundred * 100

            ten = num // 10
            if ten > 0:
                result = result + self.switch(ten, 'X', 'L', 'C')
            num = num - ten * 10

            one = num % 10
            if one > 0:
                result = result + self.switch(one, 'I', 'V', 'X')

            return result

    def switch(self, count, prefix1, prefix2, prefix3):

        result = ''
        if count <= 3:
            for i in range(0, count):
                result = result + prefix1
        elif count == 4:
            result = result + prefix1 + prefix2
        elif count >= 5 and count <= 8:
            result = result + prefix2
            for i in range(0, count - 5):
                result = result + prefix1
        else:
            result = result + prefix1 + prefix3

        return result

