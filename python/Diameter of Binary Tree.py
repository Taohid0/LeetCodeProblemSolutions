class Solution:
    def diameterOfBinaryTree(self,root):

        def dfs(root, depth=0):
            if not