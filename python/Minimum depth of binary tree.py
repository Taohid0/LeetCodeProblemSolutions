class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        depth = 0
        queue = [root, ]
        while queue:
            depth = depth + 1
            temp_queue = []
            for node in queue:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    temp_queue.append(node.left)
                if node.right:
                    temp_queue.append(node.right)
            queue = temp_queue

        return depth


treeNode = TreeNode(3)
treeNode.left = TreeNode(9)
treeNode.right = TreeNode(20)
treeNode.right.left = TreeNode(15)
treeNode.right.right = TreeNode(7)

result = Solution().minDepth(treeNode)
print(result)
