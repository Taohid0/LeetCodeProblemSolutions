class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        result = []

        def dfs(path, root):
            if not root:
                print(path)

            if root.left:
                dfs(path + [root.val, ], root.left)
            if root.right:
                dfs(path + [root.val], root.right)

            if not root.left and not root.right:
                path.append(root.val)
                result.append("->".join(str(i) for i in path))

        dfs([], root)
        return result


treeNode = TreeNode(1)
treeNode.left = TreeNode(2)
treeNode.right = TreeNode(3)
treeNode.left.right = TreeNode(5)

solution = Solution().binaryTreePaths(treeNode)
print(solution)
