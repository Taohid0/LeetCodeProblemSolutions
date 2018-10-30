class Solution:
    def tree2str(self,t):
        if not t:
            return "()"
        global result
        result = str(t.val)

        def dfs(node):
            if node.left:
                global result
                result = result+"("+str(node.val)
                dfs(node.left)
            if node.right:
                global result
                result = result