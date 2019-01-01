# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class TwoPointerListNode:
    __preNode = None
    __nextNode = None
    __own = ListNode(0)

    def __init__(self, own):
        self.__own = own

    def setPre(self, pre):
        self.__preNode = pre

    def setNext(self, next):
        self.__nextNode = next

    def getPre(self):
        return self.__preNode

    def getNext(self):
        return self.__nextNode

    def getOwn(self):
        return self.__own


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        node = head
        twoPointerHead = TwoPointerListNode(head)
        twoPointerList = twoPointerHead

        while node.next:
            nextNode = node.next
            own = TwoPointerListNode(nextNode)
            own.setPre(twoPointerList)
            twoPointerList.setNext(own)
            # next node
            node = node.next
            twoPointerList = twoPointerList.getNext()

        idx = 1

        while True:
            if idx == n:
                removeNodeNext = twoPointerList.getNext()
                removeNodePre = twoPointerList.getPre()

                if not removeNodePre:
                    return head.next

                if removeNodeNext:
                    removeNodePre.getOwn().next = removeNodeNext.getOwn()
                    return head
                else:
                    removeNodePre.getOwn().next = None
                    return head

            else:
                idx += 1
                twoPointerList = twoPointerList.getPre()
