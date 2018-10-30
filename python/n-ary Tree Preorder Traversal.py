class Solution:
    def preorder(self, root):
        if root is None:
            return []

        nodes, result = [root, ], []
        while nodes:
            root = nodes.pop()
            result.append(root.val)
            nodes= nodes+root.children[::-1]

        return result