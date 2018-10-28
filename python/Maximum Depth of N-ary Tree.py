class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        depth = 0
        nodes = [root, ]

        while nodes:
            temp_nodes = []
            depth = depth + 1
            for j in nodes:
                for i in j.children:
                    temp_nodes.append(i)
            nodes = temp_nodes

        return depth


