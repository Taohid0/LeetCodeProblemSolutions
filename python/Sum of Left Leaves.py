class Solution:
    def sumOfLeftLeaves(self, root, result=0, dir="right"):
        if not root:
            return result + 0
        if not root.left and not root.right:
            return result + (root.val if dir == "left" else 0)

        return self.sumOfLeftLeaves(root.left, result, dir="left") + self.sumOfLeftLeaves(root.right, result)
