class Solution:
    result = []

    def pathSum(self, root, sum):
        if not root:
            return []
        self.result = []
        def dfs(root, sum, nodes):
            nodes.append(root.val)
            if not root.left and not root.right and sum == root.val:
                self.result.append(nodes)
            if root.left:
                dfs(root.left, sum - root.val, nodes[:])
            if root.right:
                dfs(root.right, sum - root.val, nodes[:])

        dfs(root, sum, [])
        return self.result


class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

treeNode = TreeNode(1)
result = Solution().pathSum(treeNode,1)
print(result)
result = Solution().pathSum(treeNode,1)
print(result)