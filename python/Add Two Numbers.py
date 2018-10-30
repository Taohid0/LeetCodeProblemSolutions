class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l1
        carry = 0
        resultNode = ListNode(0)

        while l1:
            s = l1.val + l2.val + carry
            resultNode.val = s % 10
            carry = s / 10
            l1 = l1.next
            l2 = l2.next

        return l1
