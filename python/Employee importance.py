class Solution:
    def getImportance(self, employees, id):
        graph = {i.id: i for i in employees}
        importance = 0
        nodes = [id, ]
        while nodes:
            value = nodes.pop()
            importance += graph[value].importance
            nodes += graph[value].subordinates
        return importance


result = Solution().getImportance([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1)
print(result)
