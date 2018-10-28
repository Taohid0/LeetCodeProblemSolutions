class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def calculate(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        value1 = root1.val
        value2 = root2.val
        left = self.calculate(root1.left, root2.right)
        right = self.calculate(root1.right, root2.left)
        return value1 == value2 and left and right

    def isSymmetric(self, root):
        return self.calculate(root, root)


treeNode = TreeNode(1)
treeNode.left = TreeNode(2)
treeNode.right = TreeNode(2)
treeNode.left.left = TreeNode(3)
treeNode.left.right = TreeNode(4)
treeNode.right.left = TreeNode(4)
treeNode.right.right = TreeNode(3)
result = Solution().isSymmetric(treeNode)
print(result)
