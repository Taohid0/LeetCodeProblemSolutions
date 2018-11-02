class Solution:
    def deleteDuplicates(self, head):
        checkDict = {}
        firstNode = head
        while head:
            if not checkDict.get(head.val):
                checkDict[head.val] = 1
                head = head.next
            else:
                if head.next:
                    head = head.next
                else:
                    del head
        return head
