class Solution:
    def searchBST(self, root, val):
        if not root:
            return None

        def dfs(root2):
            if root2.val == val:
                return root2
            left,right = None,None
            if root2.left:
                left = dfs(root2.left)
            if root2.right:
                right = dfs(root2.right)
            if left:
                return left
            return right

        return dfs(root)
