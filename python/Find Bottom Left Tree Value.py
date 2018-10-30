class Solution:

    def findBottomLeftValue(self, root):
        if not root:
            return 0
        nodes = [root]
        result = root.val

        while nodes:
            temp_nodes = []
            for i in nodes:
                if i.right:
                    temp_nodes.append(i.right)
                if i.left:
                    temp_nodes.append(i.left)
                result = i.val
            nodes = temp_nodes

        return result

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


treeNode = TreeNode(3)
treeNode.left = TreeNode(1)
treeNode.left.left = TreeNode(0)
treeNode.left.right = TreeNode(2)
treeNode.right = TreeNode(5)
treeNode.right.left = TreeNode(4)
treeNode.right.right = TreeNode(6)

result = Solution().findBottomLeftValue(treeNode)
print(result)
