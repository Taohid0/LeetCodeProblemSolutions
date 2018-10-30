class Solution:
    def flatten(self,root):
        if not root:
            return root

        if root.left and root.right:
            self.flatten(root.left)
            self.flatten(root.right)
            root.left.right = root.right
            root.right = root.left
            root.left= None

        elif root.left:
            self.flatten(root.left)
            root.right = root.left
            root.left = None

        elif root.right:
            self.flatten(root.right)

