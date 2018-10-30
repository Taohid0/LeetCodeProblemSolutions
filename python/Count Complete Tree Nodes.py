class Solution:
    counter=0
    def countNodes(self,root):
        if not root:
            return 0

        def dfs(r):
            self.counter = self.counter +1
            if r.left:
                dfs(r.left)
            if r.right:
                dfs(r.right)

        self.counter =0
        dfs(root)
        return self.counter