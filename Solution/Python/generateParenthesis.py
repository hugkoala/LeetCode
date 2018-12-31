class Solution:

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        results = list()
        return self.recParenthesis(n, '', 0, 0)


    def recParenthesis(self, n, result, left, right):

        if left > n or right > n:
            return ''
        elif left + right == n * 2:
            # check Parenthesis
            result_str = self.checkParenthesis(result)
            if result_str == '':
                return
            else:
                return [result_str, ]
        else:
            left_list = self.recParenthesis(n, result + '(', left + 1, right)
            right_list = self.recParenthesis(n, result + ')', left, right + 1)
            results = list()

            if left_list:
                results = results + left_list
            if right_list:
                results = results + right_list
            return results

    def checkParenthesis(self, result):

        parentMap = {'(': ')'}
        stack = list()
        stack.append('#')

        idx = 0
        while not len(stack) == 0:
            char = result[idx]

            if char == '(':
                stack.append(char)
            elif char == ')':
                if char != parentMap.get(stack.pop()):
                    return ''
            idx += 1

            if idx >= len(result):
                return result
