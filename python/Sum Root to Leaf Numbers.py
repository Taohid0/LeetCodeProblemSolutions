class Solution:
    s =0
    def calculateSum(self, l):
        s = 0
        for i in l:
            s = s * 10 + i

        return s

    def sumNumbers(self, root):
        self.s = 0
        def dfs(root, nodes=[]):
            if not root:
                return 0
            nodes.append(root.val)
            if not root.left and not root.right:
                self.s = self.s + self.calculateSum(nodes)

            if root.left:
                dfs(root.left, nodes[:])
            if root.right:
                dfs(root.right, nodes[:])

        dfs(root)
        return self.s
