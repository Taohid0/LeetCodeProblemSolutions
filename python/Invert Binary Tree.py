class Solution:
    def invertTree(self, root):
        if not root:
            return root
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root
