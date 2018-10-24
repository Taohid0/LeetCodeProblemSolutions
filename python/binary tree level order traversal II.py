class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        if root is None:
            return []
        result = list()
        current_node = [root, ]

        while current_node:
            unvisited_nods = list()
            temp = list()
            for node in current_node:
                temp.append(node.val)
                if node.left:
                    unvisited_nods.append(node.left)
                if node.right:
                    unvisited_nods.append(node.right)
            current_node = unvisited_nods
            result.append(temp)

        return result[::-1]


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
result = Solution().levelOrderBottom(root)
print(result)
