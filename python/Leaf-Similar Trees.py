class Solution:
    def leafSimilar(self, root1, root2):
        leaves = []

        def dfs(root):
            if not root:
                return
            if not root.left and not root.right:
                leaves.append(root.val)
                return
            dfs(root.left)
            dfs(root.right)

        dfs(root1)
        leaves1 = leaves
        leaves = []
        dfs(root2)

        return leaves == leaves1
