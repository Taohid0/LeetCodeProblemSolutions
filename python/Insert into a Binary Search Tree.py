class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
       if not root:
           root = TreeNode(val)
           return root

       def searchBST(r):
           if r.val<val:
               