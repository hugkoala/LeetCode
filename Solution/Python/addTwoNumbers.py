# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start_node = ListNode(0)
        result = start_node
        carry = 0
        while l1 or l2 or carry:
            num1 = 0
            num2 = 0

            if l1:
                num1 = l1.val

            if l2:
                num2 = l2.val
            sum = num1 + num2 + carry

            result.next = ListNode(int(sum % 10))
            carry = (sum - sum % 10) / 10
            result = result.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return start_node.next