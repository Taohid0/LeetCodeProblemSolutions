class Solution:
    def isBipartite(self, graph):
        if not graph:
            return False
        color = [-1 for i in range(len(graph))]
        global is_bipartite
        is_bipartite = True

        def dfs(node):

            nodes = [node]
            color[0] = node

            while nodes:
                temp_nodes = []
                for i in nodes:
                    for j in graph[i]:
                        if color[j] == -1:
                            color[j] = 1 - color[i]
                            temp_nodes.append(j)
                        else:
                            if color[j] == color[i]:
                                global is_bipartite
                                is_bipartite = False
                                break
                nodes = temp_nodes
            return True

        for i in range(len(graph)):
            if color[i] == -1 and is_bipartite:
                    dfs(i)
        return is_bipartite


result = Solution().isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]])
# result = Solution().isBipartite(
#     [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9],
#      [2, 4, 5, 6, 7, 8]])
print(result)
