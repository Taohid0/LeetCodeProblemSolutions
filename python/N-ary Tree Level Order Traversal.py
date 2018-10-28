class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        nodes = [root, ]
        traversal_order = []

        traversal_order.append([root.val, ])
        while nodes:
            temp_nodes = []
            for i in nodes:
                if not i:
                    continue
                temp_nodes.append(i)
            traversal_order.append(temp_nodes)
            nodes = temp_nodes
        return traversal_order
