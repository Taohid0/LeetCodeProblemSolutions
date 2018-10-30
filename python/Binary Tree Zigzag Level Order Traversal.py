class Solution:
    def zigzagLevelOrder(self,root):
        if not root:
            return []
        result = []
        nodes = [root]
        counter = 1

        while nodes:
            temp_nodes = []
            temp_results = []
            for i in nodes:
                if i.left:
                    temp_nodes.append(i.left)
                if i.right:
                    temp_nodes.append(i.right)
                temp_results.append(i.val)
            nodes = temp_nodes

            if counter%2:
                result.append(temp_results)
            else:
                result.append(temp_results[::-1])

            counter = counter+1

        return result