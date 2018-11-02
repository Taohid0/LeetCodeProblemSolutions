class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class solution:
    def increasingBST(self,root):
        if not root:
            return root

        def dfs(r):
            if not r:
                return r
            if r.left:
                dfs(r.left)
            if r.right:
                dfs(r.right)

