import queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self,root):
        q = queue.Queue()
        q.put(root)
        q.put(root)

        while not q.empty():
            n1 = q.get()
            n2 = q.get()

            if not n1 and not n2:
                continue
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False

            q.put(n1.left)
            q.put(n2.right)
            q.put(n1.right)
            q.put(n2.left)

        return True


treeNode = TreeNode(1)
treeNode.left = TreeNode(2)
treeNode.right = TreeNode(2)
treeNode.left.left = TreeNode(3)
treeNode.left.right = TreeNode(4)
treeNode.right.left = TreeNode(4)
treeNode.right.right = TreeNode(3)
result = Solution().isSymmetric(treeNode)
print(result)
