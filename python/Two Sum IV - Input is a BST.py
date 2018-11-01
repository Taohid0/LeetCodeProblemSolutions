class Solution:

    def findTarget(self, root, k):
        if not root:
            return False
        valueDict = {}

        def dfs(r, k2):
            if not r:
                return False
            remaining = k2 - r.val

            if valueDict.get(r.val):
                return True
            valueDict[remaining] = 1
            return dfs(r.left, k2) or dfs(r.right, k2)

        result = dfs(root, k)
        return result
