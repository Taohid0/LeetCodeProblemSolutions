class Solution:
    def preorder(self, root):
        if root is None:
            return []

        nodes, output = [root, ], []
        while nodes:
            root = nodes.pop()
            output.append(root.val)
            nodes= nodes+root.children[::-1]

        return output