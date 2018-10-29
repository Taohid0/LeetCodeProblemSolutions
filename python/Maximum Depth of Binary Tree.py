class Solution:
    def maxDepth(self,root):
        if not root:
            return 0
        nodes = [root]
        depth = 0

        while nodes:
            temp_nodes = []
            depth = depth+1
            for i in nodes:
                if i.left:
                    temp_nodes.append(i.left)
                if i.right:
                    temp_nodes.append(i.right)
            nodes = temp_nodes
        return depth